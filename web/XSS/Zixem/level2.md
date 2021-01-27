# <p align="center">🎁XSS Lv.2</p>
- 문제 조건
  - 경고창에 1337 띄우기
  - 매개변수 name의 값이 화면에 그대로 들어남
  - ```script```와 ```</script>``` 필터링

- 문제풀이<br/>
  - name의 값으로 ```<script>alert(1337)</script>```입력하고 필터링 단어 확인
  - script를 대소문자를 섞어서 ScrIpt 이런식으로 아무렇게나 바꿔서 입력
  - ```<sCrIPt>alert(1337)</ScrIpT>```를 입력
  - -끝-