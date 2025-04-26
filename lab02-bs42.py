# pip install beautifulsoup4
# 혹은
# poetry add beautifulsoup4
from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = 'http://board.nyan101.com/sample/post'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# CSS 선택자를 사용하여 게시글 목록 추출
posts = soup.select('#comments-container')[0]
# 게시글 목록에서 제목 추출
texts = posts.select('div > div > p')
pprint(texts)