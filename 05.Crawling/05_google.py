import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('http://www.google.com/')
time.sleep(1) # 1초간 쉬어라 / 화면이 다 그려진다음에 작동해야하기때문에

search_box = driver.find_element_by_name('q') # search_box: 검색창
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(2)

'''html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
divs = soup.select('.g')
title_list = []; content_list = []
for div in divs:
    title = div.select_one('.LC20lb.DKV0Md').get_text()
    content = div.select_one('.aCOpRe').get_text()
    title_list.append(title)
    content_list.append(content)

df = pd.DataFrame({
    'title' : title_list, 'content': content_list
})
df.to_csv('google.csv',sep='|',encoding='utf8')'''

divs = driver.find_elements_by_css_selector('.g')
title_list = []; content_list = []
for div in divs:
    title = div.find_element_by_css_selector('.LC20lb.DKV0Md').text
    content = div.find_element_by_css_selector('.aCOpRe').text
    print(title)
    print(content)