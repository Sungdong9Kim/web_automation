import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('TV Ratings')
ws.append(['순위', '채널', '프로그램', '시청률'])

response = requests.get("https://workey.codeit.kr/ratings/index")

rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')
for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(),
        td_tags[1].get_text(),
        td_tags[2].get_text(),
        td_tags[3].get_text(),
    ]
    ws.append(row)

wb.save('시청률_20101월1주차.xlsx')
