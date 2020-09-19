from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://play.google.com/store/movies/top'

browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,1080)') # 1920 x 1080 # 모니터 해상도 높이인 1080위치로 스크롤 내리기

# 화면 가장 아래로 스크롤 내리기
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

import time
interval = 2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 화면 가장 아래로 스크롤 내리기
    time.sleep(interval) # 페이지 로딩 대기
    curr_height = browser.execute_script('return document.body.scrollHeight') # 현재 높이를 가져와서 저장

    if curr_height == prev_height:
        break

    prev_height = curr_height

print('스크롤 완료')

#######################################################################

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

# movies = soup.find_all('div',attrs = {'class':['ImZGtf mpg5gc','Vpfmgd']})
movies = soup.find_all('div',attrs = {'class':'Vpfmgd'})

print(len(movies))

for movie in movies:
    title = movie.find('div', attrs = {'class':'WsMG1c nnK0zc'}).get_text()
    # print(title)

    # 할인 전 가격
    original_price = movie.find('span', attrs={'class':'SUZt4c djCuy'})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, '<할인되지 않는 영화 제외>')
        continue

    # 할인 된 가격
    discount_price = movie.find('span',attrs = {'class' : 'VfPpfd ZdBevf i5DZme'}).get_text()
    
    # 링크
    link = movie.find('a', attrs = {'class':'JC71ub'})['href']
    # https://play.google.com + href

    print(f'제목: {title}')
    print(f'할인 전 금액: {original_price}')
    print(f'할인 후 금액: {discount_price}')
    print('링크','https://play.google.com'+link )
    print('-'*100)

browser.quit()