import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)

branch_infos = []

driver.get('https://workey.codeit.kr/orangebottle/index')
branch_tags = driver.find_elements_by_css_selector('div.branch')
for branch_tag in branch_tags:
    branch_name = branch_tag.find_element_by_css_selector('p.city').text
    address = branch_tag.find_element_by_css_selector('p.address').text
    phone_number = branch_tag.find_element_by_css_selector('span.phoneNum').text
    branch_infos.append([branch_name, address, phone_number])

driver.quit()

print(branch_infos)