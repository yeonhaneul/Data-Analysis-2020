import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 이번에는 자바스크립트가아닌 입력을 위하여 사용
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window() # bbs_list에서는 이것을 해줘야지 돌아간다. (페이지안에 페이지네이션이 보이지않으면 돌아가지 않는다.)
driver.get('http://200.1.220.254:3000/login')
time.sleep(2)

# 로그인에 아이디와 비밀번호 입력하기
driver.find_element_by_id('uid').send_keys("djy")
driver.find_element_by_css_selector('#pwd').send_keys("1234")
driver.find_element_by_class_name('btn.btn-primary').click()

# 페이지네이션 찾기
ul = driver.find_element_by_css_selector('.pagination')
lis = ul.find_elements_by_tag_name('li')
total_pages = len(lis) - 2

bids = []; titles = []; names = []
times = []; view_counts = []; reply_counts=[]
    
for page in range(total_pages):
    trs = driver.find_elements_by_tag_name('tr')
    for tr in trs[1:]:
        tds = tr.find_elements_by_tag_name('td')
        title = ''
        try:
            span = tds[1].find_element_by_tag_name('span')
            reply_count = span.text[1:-1]
            index = tds[1].text.find('[')
            title = tds[1].text[:index]
        except:
            reply_count = 0
            title = tds[1].text
        bids.append(tds[0].text)
        titles.append(title)
        names.append(tds[2].text)
        times.append(tds[3].text)
        view_counts.append(tds[4].text)
        reply_counts.append(reply_count)
    ul = driver.find_element_by_css_selector('.pagination')
    lis = ul.find_elements_by_tag_name('li')
    lis[page+2].click() # 0일 때 2페이지를 클릭하도록 (1페이지가 default이기때문에)
    time.sleep(1)

print(len(titles))