# <p align="center">🎁XSS Lv.4</p>
- 문제 조건
  - 경고창에 domain 띄우기
  - 입력칸이 있으나 활용불가
  - 나라 선택이 있으나 활용불가

- 문제풀이
  - ```<script>alert(document.domain)</script>```입력
  - 뭔가 안 되는걸 확인했으니 개발자 도구 확인
  - 나라 이름을 스크립트 코드로 바꾼 뒤 search
  - 뭔가 안 되는걸 확인했으니 다시 개발자 도구 확인
  - 나라선택 input태그 밑에 hidden 속성을 가진 input태그 확인
  - value에 ```"><script>alert(document.domain)</script><"``` 삽입 후 search
  - -끗- (chrome은 최근에 저렇게 이상하게 열고 닫으면 그냥 무효처리함)

- 부가설명
  - hidden 속성 input태그는 value의 값을 전달하기 때문에 value에 값을 넣는다.

+ chrome에서 하는 방법 찾음
  + hidden 속성을 text로 바꾸면 입력칸이 하나 더 생김
  + ```"><script>alert(document.domain)</script><"``` 입력 후 search
  + -끝-