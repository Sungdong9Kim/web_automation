import requests
from bs4 import BeautifulSoup

response = requests.get('https://workey.codeit.kr/music/index')
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

popular_searches = []

print(soup.select('ul.rank__order'))

### 코드를 작성하세요 ###
for tag in soup.select('ul.rank__order'):
    print((tag.get_text().strip()))
    print(list(tag.stripped_strings))
    print(list(tag.stripped_strings)[2])
    popular_searches.append(list(tag.stripped_strings)[2::3])

# 출력 코드
print(popular_searches)

popular_searches2 = []
for tag in soup.select('ul.rank__order li'):
    search_word = list(tag.stripped_strings)[2]
    popular_searches2.append(search_word)

print(popular_searches2)
