from selenium import webdriver

# 로딩 기다리는 라이브러리
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text('가는날 선택').click()

# 이번달 29일 출발
browser.find_elements_by_link_text('29')[0].click()

# 다음달 4일 도착
# browser.find_elements_by_link_text('4')[1].click()
browser.find_element_by_xpath('//*[@id="l_8"]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[1]/a/b').click()

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 로딩 기다리기
try: # 성공 했을 시
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[2]/div/div[4]/ul/li[1]'))) 
        # 브라우저를 최대 10초 기다려라. 어떤 element가 나올 때 까지. 그 elemnet는 xpath 기준에 해당하는
    print(elem.text)
finally: # 성공 하든 실패 하든 결국
    browser.quit()