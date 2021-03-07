import requests

# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

print(rating_page)

rating_pages = []
for i in range(5):
    url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
    response = requests.get(url)
    rating_page = response.text
    rating_pages.append(rating_page)

print(len(rating_pages))
print(rating_pages[0])