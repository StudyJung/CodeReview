# CodeReview_Include.md
- "코드는 한 번 작성되고 열 번 읽힌다." - Guido van Rossum

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
| **P1:High** | 2개 | 저장소 내부 헤더 누락, main() 빌드 차단 |
| [해결] | 0개 | - |
| **합계** | 4개 |   |

## P0:Critical - 2026/04/20

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

## P1:High - 2026/04/21

#### [P1:Build missing header][Huns][151efc0][test/Test.cpp/global/Line:1-25]
[원인] Huns.h 저장소 내부 부재
```cpp
#include "Huns.h"
생략...
	printf("T4 %d.\n ", *p5);
생략...
	printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 84, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/21</summary>
  <br>- 설명 : `test/Test.cpp`는 첫 줄에서 `Huns.h`를 포함하지만 현재 `SrcPoint` 범위 안에는 해당 로컬 헤더가 존재하지 않는다. 이 파일은 `printf`, `p5`, `pP` 같은 외부 선언 의존성이 뒤따라서, 최신 소스 기준으로는 번역 단위 자체를 재현하거나 단독 빌드할 수 없다.
  <br><br>- 의견 : `SrcPoint` 범위 리뷰를 유지하려면 필요한 로컬 헤더를 저장소 내부에 포함시키거나, 실제로 필요 없는 헤더와 외부 선언 의존성을 함께 정리해야 한다. 그렇지 않으면 이후 포인터 관련 수정 여부와 무관하게 이 파일은 계속 빌드 차단 상태로 남는다.
  <br><br>- 기타 : `if(false)` 블록 안의 `*p5`는 런타임 경로에서는 닫혀 있지만, 선언 확인은 여전히 컴파일 단계에서 필요하므로 단순한 죽은 코드 문제로 축소하면 안 된다.
 </details>

#### [P1:Compile blocker][Huns][151efc0][Test.cpp/main()/Line:25]
[원인] 미정의 포인터 pP 사용
```cpp
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 77, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/21</summary>
  <br>- 설명 : `main()` 진입 함수에서 선언되지 않은 `pP`를 즉시 역참조한다. 현재는 식별자 해석 단계에서 컴파일이 멈추고, 나중에 임시로 `pP`를 선언해도 `pT`/`pM`과 같은 nullptr 패턴으로 재발할 가능성이 높다.
  <br><br>- 의견 : 실제 필요한 변수라면 선언과 유효 초기화를 함께 추가하고, 그렇지 않으면 해당 출력 라인을 제거.
  <br><br>- 기타 : `3136b89`에서 `pM` 직접 크래시는 제거되어 해결 상태지만, `main()` 상위 진입점 기준 현재 남은 차단 이슈는 이 라인이다.
 </details>
