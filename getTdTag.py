import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

# td를 받아 앞의 4개의 td를 td_tags에 저장
# get td and store the previous 4 tds in td_tags
td_tags = soup.select('td')[:4]

for tag in td_tags:
    print(tag.get_text())