import time
from selenium import webdriver
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# wb = Workbook(write_only=True)
# ws = wb.create_sheet('코스타그램 정보')
# ws.append([''])

driver = webdriver.Chrome()

driver.get('https://workey.codeit.kr/costagram/index')

wait = WebDriverWait(driver, 3)

login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

id_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')

pw_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


posts = driver.find_elements_by_css_selector('post-list__post post')

for post in posts:
    post.click()
    time.sleep(0.5)

    driver.find_element_by_css_selector('.close-btn').click()
    time.sleep(0.5)

driver.quit()

