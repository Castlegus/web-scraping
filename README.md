# 웹 스크래핑
흔히 말하는 웹 크롤링은 사실 웹 스크래핑이라고 표현하는 것이 맞다고 합니다.

데이터 분석이나 업무 자동화에 있어서 웹 스크래핑 능력은 필수적이라고 생각하여 공부하게 되었습니다.

유튜브 '나도코딩' 채널의 [웹 스크래핑 강의](https://www.youtube.com/watch?v=yQ20jZwDjTE)를 들으며 공부한 내용입니다.

## 정규식
규칙을 가진 문자열을 표현하는 식

### 절차(순서)
1. p = re.compile('원하는 형태')
2. m = p.match('비교할 문자열) : 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search('비교할 문자열) : 주어진 문자열 중에 일치하는게 있는지 확인
4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 리스트 형태로 반환

#### 원하는 형태: 정규식
. (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)

^ (^de): 문자열의 시작 > desk, destination (O) | fade (X)

$ (se$) : 문자열의 끝 > case, base (O) | face (X)

## Requests
웹 페이지 읽어오기
- 주어진 url을 통해 받아온 html에 원하는 정보가 있을 때 사용
- res.raise_for_status()로 오류가 없는지 확인

빠르지만, 동적인 웹페이지(로딩이 있으면서 새로운 정보가 생겨나는 페이지)에는 사용이 어렵다.

## Selebium
웹 페이지 자동화
- 로그인, 필터링 등 어떤 동작을 해야하는 경우 (자동화)
- 크롬 버전에 맞는 크롬 드라이버 chromedriver.exe.가 있어야 한다.

느리고 메모리도 많이 필요하지만, 동적인 웹페이지에 사용할 수 있다.

### Selenium 사용 방법
- find_element(s)\_by\_id : id로 찾기
- find_element(s)\_by\_class_name : class name으로 찾기
- find_element(s)\_by\_link_text : 링크 text로 찾기
- find_element(s)\_by\_by_xpath : xpath로 찾기

\+
- click() : 클릭하기
- send_keys() : 글자 입력

#### 로딩 기다리기
필요 라이브러리)

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

예시) 
    
    try: # 성공 했을 시
        elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[2]/div/div[4]/ul/li[1]'))) 
          # 브라우저를 최대 10초 기다려라. 어떤 element가 나올 때 까지. 그 elemnet는 xpath 기준에 해당하는
        pass
    finally: # 성공 하든 실패 하든 결국
        browser.quit()
      
#### 스크롤 내리기
    import time
    interval = 2 # 2초에 한번씩 스크롤 내리기

    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script('return document.body.scrollHeight')

    while True:
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 화면 가장 아래로 스크롤 내리기
        time.sleep(interval) # 2초동안 페이지 로딩 대기
        curr_height = browser.execute_script('return document.body.scrollHeight') # 현재 높이를 가져와서 저장

        if curr_height == prev_height:
            break

        prev_height = curr_height

## Beautifulsoup
원하는 데이터 추출! (웹 스크래핑)

- find : 조건에 맞는 첫번째 element
- find_all : 조건에 맞는 모든 element를 리스트로
- find_next_sibling(s) # 다음 형제 찾기
- find_previous_sibling(s) # 이전 형제 찾기
- soup['href'] : 속성 값 가져오기
= soup.get.text() : 텍스트 값 가져오기

예시)

    soup = BeautifulSoup(res.text, 'lxml') 
    
    print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
    print(soup.a.attrs) # a element의 속성정보를 출력
    print(soup.a['href']) # a element의 href 속성 값 정보를 출력
    print(soup.find('a', attrs={'class':'Nbtn_upload'})) # class = 'Nbtn_upload'인 'a' element' 찾아줘
    print(soup.find(attrs={'class':'Nbtn_upload'})) # class = 'Nbtn_upload'인 '어떤' element를 찾아줘
    
    rank1 = soup.find('li', attrs={'class':'rank01'})
    print(rank1.a.get_text())

## 파일 입출력
### 이미지 가져오기
    with open('파일명', 'wb) as f:
        f.write(res.content)
### csv
    import csv
    f = open(filename, 'w', encoding='utf-8-sig', newline='')
    
## Headless Chrome
Selenium 웹 드라이버로 크롬을 사용할 때 기본으로 크롬 브라우저가 창에 뜨는데, 이 브라우저를 띄우지 않고 동작시킨다.

    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('window-size=1920x1080')

    browser = webdriver.Chrome(options=options)
    
그러나 headless Chrome을 쓰면 url 서버에서 HeadlessChrome으로 접속한 것을 알고 막을 수도 있기 때문에 이를 방지하기 위해 설정을 해준다.

    options.add_argument('user-agent=본인의 유저 에이전트')

## 주의
- 무분별한 웹 크롤링/웹 스크래핑은 대상 서버에 부하를 주기 때문에 대상 서버에서 접속자의 계정이나 IP를 차단할 수 있다.
- 스크래핑한 데이터를 무단으로 활용하면 저작권 등 침해요소가 있어 법적 제재를 받을 수 있다.

