# <p align="center">🎁XSS Lv.5</p>
- 문제 조건
  - 경고창에 1337 띄우기
  - 보통 XSS였다면 많이 봤어야할 입력 칸을 훼이크로 둠
  - 위에 매개변수 action이 구지 생김

- 문제풀이<br/>
  - Enter the name: 칸에 적용한 스크립트는 그냥 실행이 안 된다는걸 확인
  - url에 매개변수 action이 보여 임의로 값을 넣은 후 개발자 도구등을 통해 소스 확인
  - form태그가 get방식을 사용해서 action이 url로 들어난 걸 확인
  - action에 javascript:를 써서 script명령어가 가능하게 한 뒤 alert(1337) 입력
  - ```javascript:alert(1337)```
  - -끝-