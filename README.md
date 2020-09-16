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
