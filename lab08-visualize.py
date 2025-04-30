# pip install matplotlib
# pip install numpy
# 혹은
# poetry add matplotlib
# poetry add numpy
import numpy as np
import matplotlib.pyplot as plt
import requests
from tqdm import tqdm
from datetime import datetime
from pprint import pprint
import os

total_comments = []
num_posts = 100
for post_id in tqdm(range(1, num_posts + 1)):
    url = f'http://board.nyan101.com/comments/{post_id}'
    response = requests.get(url)
    comments = response.json()
    total_comments.extend(comments)

print(f'[+] get {len(total_comments)} comments')
print()

# ====== 계정별 정리 =======
print(f'[+] processing...')
user_comments = {}
for comment in total_comments:
    author_id = comment['author_id']
    # 해당 댓글이 처음 등장한 경우 빈 리스트 초기화
    if author_id not in user_comments:
        user_comments[author_id] = []
    user_comments[author_id].append(comment)

# 계정 목록 출력
print(f'[+] get {len(user_comments.keys())} users')
print(f'[+] users : {user_comments.keys()}')
print()

# ======저장 폴더 생성 =======
os.makedirs("output_images", exist_ok=True)

# ======전체 사용자 반복 시각화 ======
for target_user_id in user_comments:
    target_user_name = user_comments[target_user_id][0]['author_name']
    activity_matrix = np.zeros((24,7), dtype = int)

    for comment in user_comments[target_user_id]:
        dt = datetime.strptime(comment['created_at'], '%Y-%m-%d %H:%M')
        weekday = dt.weekday()
        hour = dt.hour
        activity_matrix[hour, weekday] += 1

    # ====== 그래프 그리기 ========
    plt.figure(figsize=(6, 8))
    # 한글폰트 깨짐 방지 (Windows에서는 'Malgun Gothic', MacOS에서는 'AppleGothic')
    #plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['font.family'] ='NanumGothic'
    plt.rcParams['axes.unicode_minus'] =False

    # 그래프 표시
    plt.imshow(activity_matrix, cmap='YlOrRd', aspect='auto')
    plt.colorbar(label='활동 횟수')

    # X축 눈금 설정(요일)
    weekdays = ['월', '화', '수', '목', '금', '토', '일']
    plt.xticks(range(7), weekdays)

    # Y축 눈금 설정(시간대)
    hours = [f'{i:02d}' for i in range(24)]
    plt.yticks(range(24), hours)

    # 그래프 제목 설정
    plt.title(f'User #{target_user_id}({target_user_name})의 활동 패턴')

    # 각 칸에 숫자 표시
    """
    for hour in range(24):
        for weekday in range(7):
            if activity_matrix[hour, weekday] > 0:
                plt.text(weekday, hour, str(activity_matrix[hour, weekday]), ha='center', va='center', color='black')
    """
    plt.tight_layout()

    #======저장=========
    sanitized_name = ''.join(c for c in target_user_name if c.isalnum() or c in ' _-')
    filename = f"output_images/{target_user_id}({sanitized_name}).png"
    plt.savefig(filename, dpi=300, bbox_inches = 'tight')
    plt.close()
print("\n 모든 사용자 그래프 저장이 완료됨")

