# <p align="center">🎁XSS Lv.2</p>
- 문제 조건
  - 경고창에 domain 띄우기
  - 그냥 하라고 입력칸이 있음

- 문제풀이<br/>
  - ```<script>alert(document.domain)</script>```입력
  - 뭔가 안 되는걸 확인했으니 개발자 도구 확인
  - form 태그에 입력한 내용이 그대로 들어감
  - ">로 form 태그를 닫고 그 뒤에 스크립트 삽입
  - ```"><script>alert(document.domain)</script>```
  - -끗-