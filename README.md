# 웹 스크래핑
유튜브 '나도코딩' 채널의 [웹 스크래핑 강의](https://www.youtube.com/watch?v=yQ20jZwDjTE)를 들으며 공부한 내용

## 정규식
### 절차(순서)
1. p = re.compile('원하는 형태')
2. m = p.match('비교할 문자열) : 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search('비교할 문자열) : 주어진 문자열 중에 일치하는게 있는지 확인
4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 리스트 형태로 반환

#### 원하는 형태: 정규식
. (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)

^ (^de): 문자열의 시작 > desk, destination (O) | fade (X)

$ (se$) : 문자열의 끝 > case, base (O) | face (X)

## Beautifulsoup
print(soup.a) # soup 객체에서 처음 발견되는 a element 출력

print(soup.a.attrs) # a element의 속성정보를 출력

print(soup.a['href']) # a element의 href 속성 값 정보를 출력

print(soup.find('a', attrs={'class':'Nbtn_upload'})) # class = 'Nbtn_upload'인 'a' element' 찾아줘

print(soup.find(attrs={'class':'Nbtn_upload'})) # class = 'Nbtn_upload'인 '어떤' element를 찾아줘
