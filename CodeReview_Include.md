## P0:Critical - 2026/04/19

#### [P0:Undefined symbol][정훈희][3136b89][Test.cpp/main()/Line:23]
[원인] 미정의 식별자 pP 역참조
```cpp
printf("T3 %d.\n ", *pP);
```
[추천] pP 선언 추가 또는 라인 제거
```cpp
int P = 0;
int* pP = &P;
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`가 선언되지 않은 식별자로 `main()`에서 역참조 사용되어 컴파일 오류 발생. `Huns.h` 헤더 누락과 겹쳐 빌드 자체 불가.
  <br><br>- 의견 : `pP`를 선언하거나 해당 라인 제거.
  <br><br>- 기타 : `*pT`, `*pM`과 동일 패턴의 미정의 포인터 역참조. 유사 심볼 `p5`도 line 9에 존재.
 </details>

#### [P0:Include missing][정훈희][3136b89][Test.cpp/global/Line:1]
[원인] Huns.h 헤더 파일 존재하지 않음
```cpp
#include "Huns.h"
```
[추천] 존재하는 헤더로 교체
```cpp
#include "Test.h"
```
 <details>
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `test/Huns.h` 파일이 저장소에 없음. `test/Test.h`만 존재. 헤더 해석 불가로 컴파일 불가.
  <br><br>- 의견 : `Test.h`로 교체 또는 `Huns.h` 파일 신규 생성.
  <br><br>- 기타 : `Test.h`는 `#include "Tests.h"`를 포함하고 있으나 `Tests.h`도 저장소에 없음. 연쇄적 헤더 누락 문제.
 </details>

#### [P0:Crash nullptr][정훈희][f625d50a][Test.cpp/main()/Line:23]
[원인] pM nullptr 역참조 런타임 크래시
```
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
[해결] nullptr 역참조 라인 제거
```
int* pM = nullptr;

printf("T2 %d.\n ", 123);
```
 <details>
  <summary>상태 : [해결] , 위험 : 88, 횟수 : 3, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `main()` 함수에서 `pM`을 `nullptr`로 초기화한 직후 체크 없이 역참조. 프로그램 진입점에서 즉시 크래시 발생. `151efc0` 커밋부터 존재하는 이슈.
  <br><br>- 의견 : `pM` 역참조 전 nullptr 체크 추가 또는 유효한 포인터 할당 후 사용.
  <br><br>- 기타 : `main()` 내 `*pP`(미선언)도 유사한 역참조 문제 존재.
 </details>
 - 사유 : 커밋 3136b89에서 `printf("T1 %d.\n ", *pM);` 라인 삭제로 해결

#### [P0:Undefined symbol][정훈희][3136b89][Test.cpp/TEST()/Line:9]
[원인] 데드코드 내 미선언 변수 p5 컴파일 에러
```cpp
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
[추천] dead code 블록 제거
```cpp
// if(false) 블록 전체 제거
```
 <details>
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `p5`가 선언되지 않은 식별자로 `TEST()`에서 역참조. `if(false)` 내부이지만 컴파일 대상이므로 빌드 오류 발생. 이중 공백(`if(  false)`)으로 코드 품질도 낮음.
  <br><br>- 의견 : dead code `if(false)` 블록 제거 또는 `p5`를 유효 포인터로 교체.
  <br><br>- 기타 : `*pP`(미선언)과 동일한 미선언 변수 패턴. 데드코드이므로 런타임 영향은 없으나 컴파일 에러로 빌드 차단.
 </details>
