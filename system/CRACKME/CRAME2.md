<h1 align="center">⚒ crackme 2</h1>

### ☑ 풀이 : 

- **문제 조건**
1. 시리얼 값 얻기 or 성공 메세지 띄우기
- **문제 풀이**
1. 일단 실행파일을 열어서 이것 저것 정보를 캐냄
   - Name은 4자리 이상
   - About은 생성 날짜
   - Quit 나가기
   - Serial이 맞지 않을 경우 Nope, this serial is wrong! 출력
2. 사용할 디버거를 아무거나 킴(저는 x64dbg를 사용)
3. 분석을 위해 우리가 아는 문자열인 Nope, this serial is wrong!을 검색 후 이동
4. 위쪽에 ```je crackme2.403408```이라는 명령줄이 있음
   - 이게 실행이 되면 Conguratulations와 Yep, this key is right!이라는 구문을 건너뛰고 실패 커맨드로 이동함
5. 그럼 실행이 안 되게 해야하기 때문에 기존에 틀렸을때 실행되던 je(equal일때 실행)에서 jne(equal이 아닐 경우 실행으로 변경)
6. 파일을 패치하고 실행해봤을 때, 아무 시리얼 값을 넣고 Check를 누르면 성공 메세지 출력