# CodeReview_정훈희.md
- "명료함은 프로그래밍의 가장 중요한 덕목이다." - Brian Kernighan

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **누적 Output** | CodeReview_20260421_1776776201.md |
| **Period** | 2026/04/19 11:41:23 - 2026/04/20 08:25:39 |
| **Model(Effort)** | gpt-5.4 (Codex) |
| **Tools** | '/review', `git diff`, `git log`, `Get-Content` |

| 등급 | 건수 | 설명 |
| :--- | :--- | :--- |
| **P0:Critical** | 2개 | 2차 헤더 체인, dead code 컴파일 차단 |
| **합계** | 2개 |   |

## P0:Critical - 2026/04/21

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
  <summary>상태 : [미결] , 위험 : 88, 횟수 : 5, 추적 : 2026/04/19 - 2026/04/20</summary>
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
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 8, 추적 : 2026/04/19 - 2026/04/20</summary>
  <br>- 설명 : `p5`가 선언되지 않은 식별자로 `TEST()`에서 역참조. `if(false)` 내부이지만 컴파일 대상이므로 빌드 오류 발생. 이중 공백(`if(  false)`)으로 코드 품질도 낮음.
  <br><br>- 의견 : dead code `if(false)` 블록 제거 또는 `p5`를 유효 포인터로 교체.
  <br><br>- 기타 : `*pP`(미선언)과 동일한 미선언 변수 패턴. 데드코드이므로 런타임 영향은 없으나 컴파일 에러로 빌드 차단.
 </details>
