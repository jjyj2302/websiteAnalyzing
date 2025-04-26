import requests
from bs4 import BeautifulSoup
from pprint import pprint

total_titles = []
total_writers = []
num_pages = 10
for page in range(1, num_pages + 1):
    print(f'[+] load page {page}...')
    url = f'http://board.nyan101.com/list/{page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # CSS 선택자를 사용하여 게시글 목록 추출
    posts = soup.select('body > div > div.bg-white.rounded-lg.shadow-md.p-6 > ul')[0]
    
    # 게시글 목록에서 제목 추출
    titles = posts.select('li > a > div > h3')
    writers = posts.select('li > a > p')
    total_titles.extend(titles)
    total_writers.extend(writers)
pprint(total_titles)
pprint(total_writers)
print(f'[+] get {len(total_titles)} posts')
print(f'[+] get {len(total_writers)} writers')