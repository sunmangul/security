# <p align="center">old_05</p>
> - 문제풀이
>> - 문제 조건
>> 1. Login을 눌렀을때 ~mem/login.php로 이동
>> 2. mem 디렉토리로 이동해보면 join.php로 접근 가능
>> 3. script 코드를 확인하면 난독화 되어있음<br/>
>> -> 정리했을 때, 쿠키명은 oldzombie, url은 mode=1이라고 한다.
>> 4. admin이라는 id로 로그인해야 하지만 이미 admin이 존재
>
>> - 문제 풀이
>> 1. 무작위 값이 들어간 이름이 oldzombie인 쿠키 추가
>> 2. 그냥 admin이 있으니 id 앞이나 뒤에 null(%00) 혹은 공백 추가
>> 3. 순조로운 회원가입과 로그인
>
>> - 추가 설명
>> 1. js 난독화는 beautiful js라고 치면 코드를 정리해주는 사이트가 존재
>> 2. 정리된 코드에서 oldzombie 쿠키가 없으면 bye 출력
>> 3. url에 mode=1이 없으면 access_denied만 출력