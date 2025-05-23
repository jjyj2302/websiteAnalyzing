# pip install selenium
# pip install webdriver-manager
# 혹은
# poetry add selenium
# poetry add webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pprint import pprint
import time

# 웹드라이버 설정 (버전에 맞는 ChromDriver를 자동으로 다운로드)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())

# 게시글 페이지 로드
num_posts = 100
for post_id in tqdm(range(1, num_posts + 1)):
    driver.get(f'http://board.nyan101.com/comments/{post_id}')
    driver.implicitly_wait(10) 
    # 댓글이 동적으로 로딩될 때까지 기다릴 여유시간 설정 (10초)
    comments = driver.find_elements(By.CLASS_NAME, 'comment')

    for comment in comments:
        print(comment.text)
        author = comment.find_element(By.CLASS_NAME, 'comment-author-name').text
        print(f'[+] 추출된 author-name: {author}')
        print()


# 즉시 종료 방지용
time.sleep(3)
from tqdm import tqdm
import requests
from pprint import pprint

total_comments = []
num_posts = 100
for post_id in tqdm(range(1, num_posts + 1)):
    url = f'http://board.nyan101.com/comments/{post_id}'
    response = requests.get(url)
    comments = response.json()
    total_comments.extend(comments)

pprint(total_comments)
print(f'[+] get {len(total_comments)} comments')
