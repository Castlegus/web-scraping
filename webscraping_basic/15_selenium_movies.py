import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
"Accept-Language":'ko-KR,ko'}

url = 'https://play.google.com/store/movies/top'

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
movies = soup.find_all('div',attrs = {'class':'ImZGtf mpg5gc'}) # html 정보
print(len(movies)) # 10개만 가져오게 된다.

# with open('movie.html','w', encoding='utf8') as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find('div', attrs = {'class':'WsMG1c nnK0zc'}).get_text()
    print(title)

# 그러나 requests로는 처음에 불러와지는 10개의 데이터만 가져오게 된다.
# 동적으로 스크롤을 내렸을 때 로딩 후 불러오는 데이터에 대해서 가져오기 위해서는 selenium을 사용한다.