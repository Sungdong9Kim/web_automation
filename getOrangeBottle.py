import requests
from bs4 import BeautifulSoup

### 코드를 작성하세요 ###
response = requests.get('https://workey.codeit.kr/orangebottle/index')
bottle_page = response.text

soup = BeautifulSoup(bottle_page, 'html.parser')

wanted_list = soup.select('.branch > p.city')
#wanted_list_with_p = wanted_list.select('p')
name_list = []
phone_number_list = []
for city in wanted_list:
    name_list.append(city)

print(wanted_list)
#print(wanted_list_with_p)

# 출력 코드
#print(branch_infos)