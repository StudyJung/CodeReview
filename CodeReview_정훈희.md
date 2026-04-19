# CodeReview_정훈희.md
- "먼저 작동하게 만들고, 그 다음 올바르게 만들고, 그 다음 빠르게 만들어라." - Kent Beck

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **누적 Output** | CodeReview_20260419_1776642516.md |
| **Period** | 2026/04/19 22:58:18 - 2026/04/20 08:44:01 |
| **Model(Effort)** | claude-opus-4-7 (--effort max) |
| **Tools** | '/check' |

| 등급 | 건수 | 설명 |
| :--- | :--- | :--- |
| **P0:Critical** | 5개 | nullptr 역참조, 미정의 심볼, 헤더 누락 |
| **합계** | 5개 |   |

## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][3136b89][Test.cpp/TEST()/Line:5-12]
[원인] pT nullptr 초기화 후 역참조 크래시
```cpp
int* pT = nullptr;

if(  false)
{
	printf("T4 %d.\n ", *p5);
}

printf("T5 %d.\n ", *pT);
```
[추천] 역참조 전 nullptr 체크 추가
```cpp
int* pT = nullptr;

if (pT != nullptr)
{
	printf("T5 %d.\n ", *pT);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 99, 횟수 : 5, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 후 line 12에서 `*pT`로 역참조하여 런타임 크래시 발생. `int TEST()` 함수 진입 시 dead code 블록을 지나 즉시 크래시.
  <br><br>- 의견 : 역참조 전 `nullptr` 체크 추가 또는 유효 포인터 할당 필요. 함수 자체가 테스트 목적이면 함수 제거 고려.
  <br><br>- 기타 : 커밋 `b41368f`에서 T7 `*pT` 역참조가 추가로 재도입되어 동일 변수에 대한 중복 위험. Exclude의 T7(Line:10) 기존 제외 항목은 `2722022`에서 삭제되어 별도 P0 이슈로 재생성. `main()`의 `*pP`와 동일 패턴 연쇄.
 </details>

#### [P0:Undefined symbol][정훈희][3136b89][Test.cpp/main()/Line:25]
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
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 7, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`가 선언되지 않은 식별자로 `main()`에서 역참조 사용되어 컴파일 오류 발생. `Huns.h` 헤더 누락과 겹쳐 빌드 자체 불가. 커밋 `b41368f`에서 T7 라인이 추가되면서 라인 번호가 23 → 25로 이동.
  <br><br>- 의견 : `pP`를 선언하거나 해당 라인 제거.
  <br><br>- 기타 : `*pT`, `*pM`과 동일 패턴의 미정의/nullptr 포인터 역참조. 유사 심볼 `p5`도 line 9에 존재.
 </details>

#### [P0:Include missing][정훈희][5af0c3a][Test.cpp/global/Line:1]
[원인] Huns.h 헤더 파일 존재하지 않음
```cpp
#include "Huns.h"
```
[추천] 존재하는 헤더로 교체
```cpp
#include "Test.h"
```
 <details>
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 6, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `test/Huns.h` 파일이 저장소에 없음. `test/Test.h`만 존재. 헤더 해석 불가로 컴파일 불가.
  <br><br>- 의견 : `Test.h`로 교체 또는 `Huns.h` 파일 신규 생성.
  <br><br>- 기타 : `Test.h`는 `#include "Tests.h"`를 포함하고 있으나 `Tests.h`도 저장소에 없음. 연쇄적 헤더 누락 문제.
 </details>

#### [P0:Include missing][정훈희][5af0c3a][Test.h/global/Line:3]
[원인] Tests.h 헤더 파일 존재하지 않음
```cpp
#include "Tests.h"
```
[추천] 존재하는 헤더로 교체 또는 라인 제거
```cpp
// #include "Tests.h" 제거 또는 실제 존재하는 헤더로 교체
```
 <details>
  <summary>상태 : [미결] , 위험 : 88, 횟수 : 4, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `test/Tests.h` 파일이 저장소에 없음. `Test.h`에서 `#include "Tests.h"`로 포함 시도하여 컴파일 불가. `Test.cpp`가 `Huns.h`를 포함하고 `Huns.h`가 존재한다면 간접적으로 이 오류가 전파됨.
  <br><br>- 의견 : 라인 제거 또는 실제 존재하는 헤더로 교체.
  <br><br>- 기타 : `Test.cpp`의 `#include "Huns.h"` 문제와 함께 2단계 헤더 누락 체인을 형성.
 </details>

#### [P0:Undefined symbol][정훈희][5af0c3a][Test.cpp/TEST()/Line:9]
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
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 7, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `p5`가 선언되지 않은 식별자로 `TEST()`에서 역참조. `if(false)` 내부이지만 컴파일 대상이므로 빌드 오류 발생. 이중 공백(`if(  false)`)으로 코드 품질도 낮음.
  <br><br>- 의견 : dead code `if(false)` 블록 제거 또는 `p5`를 유효 포인터로 교체.
  <br><br>- 기타 : `*pP`(미선언)과 동일한 미선언 변수 패턴. 데드코드이므로 런타임 영향은 없으나 컴파일 에러로 빌드 차단.
 </details>
