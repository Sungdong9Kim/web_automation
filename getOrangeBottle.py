import requests
from bs4 import BeautifulSoup

### 코드를 작성하세요 ###
response = requests.get('https://workey.codeit.kr/orangebottle/index')
bottle_page = response.text

soup = BeautifulSoup(bottle_page, 'html.parser')

branch_infos = []

branch_tags = soup.select('div.branch')

for branch_tag in branch_tags:
    branch_name = branch_tag.select_one('p.city').get_text()
    address = branch_tag.select_one('p.address').get_text()
    phone_number = branch_tag.select_one('span.phoneNum').get_text()
    branch_infos.append([branch_name, address, phone_number])

print(branch_infos)

# wanted_list = soup.select('.branch > p.city')
# #wanted_list_with_p = wanted_list.select('p')
# name = soup.select('.branch > p.ave')
# number = soup.select('span.phoneNum')
# name_list = []
# phone_number_list = []
# for city in wanted_list:
#     name_list.append(city)
# for num in number:
#     phone_number_list.append(number)
#
# print(wanted_list)
# print(phone_number_list)
# #print(wanted_list_with_p)
#
# for city in name_list:


# 출력 코드
#print(branch_infos)