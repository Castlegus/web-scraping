import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    return soup
    

def scrape_weather():
    print(['오늘 서초구 날씨'])

    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%B4%88%EA%B5%AC+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%B4%88%EA%B5%AC&tqi=U2l%2BLdp0J1ZssNEnWZssssssteK-306107'

    soup = create_soup(url)

    # 흐림, 어제보다 xx도 높아요
    cast = soup.find('p',attrs={'class':'cast_txt'}).get_text()
    # 현재 xx도
    curr_temp = soup.find('p',attrs={'class':'info_temperature'}).get_text().replace('도씨','')
    # 최저 온도
    min_temp = soup.find('span',attrs={'class':'min'}).get_text()
    # 최고 온도
    max_temp = soup.find('span',attrs={'class':'max'}).get_text()
    # 오전 강수 확률 xx%
    morning_rain_rate = soup.find('span',attrs={'class':'point_time morning'}).get_text().strip()
    # 오후 강수 확률 xx%
    afternoon_rain_rate = soup.find('span',attrs={'class':'point_time afternoon'}).get_text().strip()

    # 미세먼지 정보
    dust = soup.find('dl',attrs={'class':'indicator'})
    미세먼지 = dust.find_all('dd')[0].get_text()
    초미세먼지 = dust.find_all('dd')[1].get_text()
    오존지수 = dust.find_all('dd')[2].get_text()


    # 출력
    print(cast)
    print(f'현재 {curr_temp} (최저 {min_temp} / 최고 {max_temp})')
    print(f'오전 {morning_rain_rate} / 오후 {afternoon_rain_rate}')
    print()
    print(f'미세먼지 {미세먼지}')
    print(f'초미세먼지 {초미세먼지}')
    print(f'오존지수 {오존지수}')
    print()

def scrape_headline_news():
    print('[헤드라인 뉴스]')

    url = 'https://news.naver.com'

    soup = create_soup(url)

    news_list = soup.find('ul',attrs={'class':'hdline_article_list'}).find_all('li',limit=5) # 5개만 찾아라
    for index, news in enumerate(news_list):
        title = news.find('a').get_text().strip()
        link = url + news.find('a')['href']
        print(f'{index+1}. {title}')
        print(f' 링크 : {link}')
        print()

def scrape_IT_news():
    print('[IT 일반 최신 뉴스]')

    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = create_soup(url)
    news_list = soup.find('ul', attrs={'class':'type06_headline'}).find_all('li',limit=3)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find('img')
        if img: # img 태그가 있다면
            a_idx = 1 # 1번째 a 태그의 정보를 사용

        title = news.find_all('a')[a_idx].get_text().strip()
        link = news.find_all('a')[a_idx]['href']
        print(f'{index+1}. {title}')
        print(f' 링크 : {link}')
        print()


def scrape_English():
    print('[해커스 오늘의 영어 회화]')
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    soup = create_soup(url)
    sentences = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})
    print('(영어 지문)')
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, index 기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
    print()

    print('(한글 지문)')
    for sentence in sentences[:len(sentences)//2]:# 8문장이 있다고 가정할 때, index 기준 0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())


if __name__ == '__main__':

    print('기준 시간: ', datetime.now())

    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 5개 가져오기
    scrape_IT_news() # IT 일반 최신 뉴스 3개 가져오기
    scrape_English()