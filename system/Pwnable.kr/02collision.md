<h1 align="center">🍬02.collustion</h1>

### ☑ 풀이 : 

- **문제 조건**
1. flag값 얻기

- **준비물**
1. 16진수 계산기(Speed Crunch 사용)
- **문제 풀이**
1. 현재 위치 파일, 디렉토리 확인
  ```ls -alF``` (숨겨진 파일, 디렉토리를 자세하게 보여줌 + 실행파일 확인)
2. 유일하게 확인 가능한 파일인 col.c 내용 출력
  ```cat col.c```
3. 코드 분석
```C
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;  // 매개변수 정수형으로
        int i;              
        int res=0;
        for(i=0; i<5; i++){ // 4byte씩 5번(20byte) 읽음
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){      // 값의 길이가 20byte가 되는지 검증
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){  // 입력값과 hashcode 값이 같으면 플래그 출력
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```
4. 일단 위 코드대로 4byte(int)씩 5번 입력을 받기 때문에 heshcode를 5로 나눠준다.
   ```0x21DD09EC = 568134124```10진수로 바꿔주는 이유는 16진수에서 연산하면 .CCCCCC...가 나온다.
   ```568134124 / 5 = 113626824.8```
   ```hex(113626824) = 0x6C5CEC8``` ```hex(113626824+4) = 0x6C5CECC```
5. 이 계산 결과를 한줄로 매개변수로 넘겨야하기 때문에 파이썬을 사용하겠다.
    ```./col $(python -c 'print "\xc8\xce\xc5\x06"*4+"\xcc\xce\xc5\x06"')```
리틀엔디언 방식이기 때문에 두개씩 끊고 뒤에서 부터 작성
- **플래그**
```daddy! I just managed to create a hash collision :)```