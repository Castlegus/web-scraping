from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

# headless Chrome을 쓰면 url 서버에서 HeadlessChrome으로 접속한 것을 알고 막을 수도 있기 때문에 이를 방지하기 위해 설정을 해준다.
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')


browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

browser.get(url)

detected_value = browser.find_element_by_id('detected_value')

print(detected_value.text)
browser.quit()