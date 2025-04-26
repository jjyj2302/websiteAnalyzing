import requests

url="  http://board.nyan101.com/sample/post"
headers = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
response=requests.get(url, headers=headers, verify=False)
print(response.text)
