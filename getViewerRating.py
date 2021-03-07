import requests

rating_pages = []

for i in range(9):
    for j in range(12):
        for k in range(5):
            url = f'https://workey.codeit.kr/ratings/index?year=201{i}&month={j+1}&weekIndex={k}'
            response = requests.get(url)
            rating_page = response.text
            rating_pages.append(rating_page)


print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드
print("hi")
