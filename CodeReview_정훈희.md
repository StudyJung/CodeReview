## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][896f4c5][Test.cpp/TEST()/Line:7]
`TEST()`에서 `nullptr`로 초기화한 `pT`를 `*pT`로 역참조하여 호출 즉시 SIGSEGV
``` 문제 코드
int* pT = nullptr;

printf("T4 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 3, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr` 초기값 그대로 유지된 채 `printf`의 가변 인자로 `*pT`가 평가됨. `TEST()`가 호출되는 모든 경로에서 SIGSEGV 발생. `896f4c5 (ccc)` 커밋이 `//printf` 주석을 해제하며 활성화됨
  <br><br>- 의견 : 포인터가 불필요하면 `int nT = 0; printf("T4 %d.\n ", nT);`로 교체. 포인터 경로가 의도라면 유효한 변수 주소(`&val`)로 초기화하고 nullptr 가드 추가
  <br><br>- 기타 : 동일 커밋에서 `main()` Line:21에도 동일 패턴이 함께 활성화됨. 하나의 주석 해제 커밋이 두 개의 P0 크래시를 동시에 심은 구조. 커밋 메시지 "ccc"에 변경 의도가 없어 위험 인지 불가
 </details>

## P1:High - 2026/04/19

#### [P1:Undefined identifier][정훈희][896f4c5][Test.cpp/main()/Line:25]
`main()` 활성 경로에서 미선언 식별자 `pP` 역참조
``` 문제 코드
	int* pM = nullptr;

	//printf("T1 %d.\n ", *pM);

	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 80, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`는 `main()` 포함 어느 스코프에도 선언되어 있지 않음. 엄격 빌드에서 컴파일 차단. 링크가 성공한다면 임의 전역 심볼을 역참조해 크래시. `896f4c5 (ccc)` 커밋의 주석 해제 토글이 인접 라인(Line:21)에만 적용되며 동일 파일의 dead-line `*pP` 가 그대로 잔존
  <br><br>- 의견 : 사용 의도가 없으면 라인 삭제. 유지 필요 시 `int nP = 0; printf("T3 %d.\n ", nP);` 등 선언·초기화 후 사용
  <br><br>- 기타 : 동일 파일의 dead branch 내 `*p5` 와 같은 계열 실수. 무의미한 커밋 메시지("ccc", "ㅌㅌ") 가 반복되어 리뷰·롤백 근거 확보가 어려움
 </details>

#### [P1:Missing header][정훈희][151efc0][Test.cpp/global/Line:1]
존재하지 않는 헤더 `Huns.h` 포함 — Test.cpp 빌드 자체 불가
``` 문제 코드
#include "Huns.h"

int TEST()
{
	int* pT = nullptr;
```
 <details>
  <summary>상태 : [미결] , 위험 : 70, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 리포지토리에 `Huns.h` 파일이 존재하지 않음. Test.cpp 의 모든 후속 이슈가 런타임 이전 단계에서 막힘
  <br><br>- 의견 : 이 파일은 `printf` 만 사용하므로 `#include <cstdio>` 로 교체. 실제 의도한 의존 헤더가 있다면 리포지토리에 파일을 추가하거나 경로를 바로잡음
  <br><br>- 기타 : HEAD 기준 이슈(RV2). 범위(test1..HEAD) 내 커밋이 아닌 최초 업로드(151efc0)로부터 유입
 </details>

#### [P1:Missing header][정훈희][151efc0][Test.h/global/Line:3]
헤더 파일에서 존재하지 않는 `Tests.h` 포함 — 포함하는 모든 TU 빌드 불가
``` 문제 코드
#include <iostream>

#include "Tests.h"

using namespace std;
```
 <details>
  <summary>상태 : [미결] , 위험 : 70, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 리포지토리에 `Tests.h` 파일이 존재하지 않음. `Test.h` 를 포함하는 모든 TU 가 동시에 빌드 실패
  <br><br>- 의견 : include 삭제. 헤더 가드로 `#pragma once` 만 남기고 실제 의존만 최소로 유지
  <br><br>- 기타 : 자기 파일명 `Test.h` 와 유사해 오타로 유입된 정황
 </details>
