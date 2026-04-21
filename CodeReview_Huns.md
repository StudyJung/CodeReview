# CodeReview_Huns.md
- "프로그램을 잘 짜는 유일한 방법은 그것을 다시 짜는 것이다." - Fred Brooks

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **누적 Output** | CodeReview_20260421_1776776201.md |
| **Period** | 2026/04/19 11:41:23 - 2026/04/20 08:25:39 |
| **Model(Effort)** | gpt-5.4 (Codex) |
| **Tools** | '/review', `git diff`, `git log`, `Get-Content` |

| 등급 | 건수 | 설명 |
| :--- | :--- | :--- |
| **P1:High** | 2개 | main() 빌드 차단, 저장소 헤더 누락 |
| **합계** | 2개 |   |

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
  <br>- 설명 : `test/Test.cpp`는 첫 줄에서 `Huns.h`를 포함하지만 현재 `SrcPoint` 범위 안에는 해당 로컬 헤더가 없다. 번역 단위가 시작 단계에서 깨지므로 `printf`, `p5`, `pP` 같은 후속 의존성 이전에 파일 단독 빌드가 바로 막힌다.
  <br><br>- 의견 : 실제 의도가 `Test.h`라면 include 대상을 교체하고, 별도 헤더가 필요하다면 저장소 내부에 추가해 필요한 선언을 닫아야 한다.
  <br><br>- 기타 : 이 문제를 정리해도 `test/Test.h`의 `Tests.h` 누락이 이어지므로 헤더 체인을 함께 정리해야 한다.
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
