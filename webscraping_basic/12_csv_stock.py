import requests
import csv
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

filename = '시가총액 1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') # csv 파일에서 글자가 깨지면 'utf-8-sig'
writer = csv.writer(f)

title='N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url+str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
    for row in data_rows: # tr 정보들 중에서
        columns = row.find_all('td') # td 정보들을 columns에 저장
        if len(columns) <= 1: # 만약 tr 내에 있는 td가 1개 이하라면
            continue # (의미 없는 데이터 skip)
        data = [column.get_text().strip() for column in columns] # columns에 있는 것들을 하나씩 가져와서 이름은 column이라고 하고
                                                                 # 그 칼럼에서 get_text()를 해 온다.
        # print(data)
        writer.writerow(data)