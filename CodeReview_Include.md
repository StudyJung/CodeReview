## P0:Critical - 2026/04/19


#### [P0:Crash nullptr][정훈희][151efc0][Test.cpp/TEST()/Line:5-7]
pT nullptr 역참조 크래시
```cpp
int* pT = nullptr;

printf("T4 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [해결] , 위험 : 99, 횟수 : 17, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 직후 `*pT`로 역참조하여 `TEST()` 진입 즉시 크래시 발생. 실제 실행 경로에 위치하며 회피 불가
  <br><br>- 의견 : `pT`에 유효한 메모리를 할당하거나, 출력 목적이라면 포인터가 아닌 정수 변수 `int nT = 0;`으로 변경
  <br><br>- 기타 : TEST() 내 동일 패턴의 `*p5`(Line:11)와 연계 — TEST() 전체 실행 불가 상태
 </details>
 - 사유 : aae2843에서 `printf("T4 %d.\n ", *pT);` 주석 처리로 null 역참조 비활성화

#### [P0:Compile undeclared][정훈희][151efc0][Test.cpp/main()/Line:25]
미선언 식별자 pP 역참조로 컴파일 실패
```cpp
printf("T2 %d.\n ", 123);

printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 18, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `main()` 내에서 `pP`가 선언되지 않은 상태로 `*pP` 역참조가 수행되어 컴파일 에러(undeclared identifier) 발생. 빌드 단계에서 차단됨. aae2843에서 `*pM` 크래시 라인은 주석 처리되었으나 `*pP` 라인은 여전히 활성 상태로 잔존. 이전 커밋에서 주석으로 비활성화되어 있던 `*pP` 역참조가 활성화된 회귀(regression)
  <br><br>- 의견 : `pP` 참조가 필요하다면 `main()` 내에 선언 및 초기화, 불필요하면 해당 라인 제거 또는 주석 처리
  <br><br>- 기타 : 설령 `pP`가 선언되더라도 nullptr로 초기화되면 같은 파일 TEST()의 `*pT` 크래시와 동일한 패턴으로 런타임 위험 존재
 </details>

#### [P0:Compile undeclared][정훈희][151efc0][Test.cpp/TEST()/Line:11]
미선언 식별자 p5 역참조로 컴파일 실패
```cpp
if(  false)
{
	printf("T5 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 18, 추적 : 2026/04/18 - 2026/04/19</summary>
  <br>- 설명 : `p5`가 `TEST()` 스코프 및 전역에 선언되어 있지 않음. `if(false)` 분기는 실행되지 않지만 컴파일 단계에서 반드시 파싱되어 에러 발생. 해당 블록은 영구 데드 코드이나 컴파일러는 토큰을 해석함. Huns02 시점 `*pT`(미선언)에서 `*p5`(미선언)으로 변수명만 변경된 이력 존재
  <br><br>- 의견 : 죽은 분기 자체를 제거하거나, 필요 시 `TEST()` 내에 `p5` 선언 및 초기화
  <br><br>- 기타 : `if(  false)`의 이중 공백도 스타일 문제 — 블록 제거 시 함께 정리 가능. Line:7 `*pT` 크래시와 병행 — TEST() 전체 컴파일 불가 상태
 </details>

#### [P0:Compile include][정훈희][151efc0][Test.cpp/global/Line:1]
존재하지 않는 헤더 Huns.h include로 컴파일 실패
```cpp
#include "Huns.h"
```
 <details>
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 18, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `Huns.h`가 저장소에 존재하지 않음. 이 파일을 포함하는 모든 TU가 빌드 불가. 기존 `"Test.h"`에서 `"Huns.h"`로 변경되었으나 해당 헤더가 생성되지 않은 상태. `printf` 사용을 위해 `<cstdio>` 등 표준 헤더도 누락된 상태
  <br><br>- 의견 : `"Test.h"`로 복구하거나, `Huns.h`를 생성하여 필요한 선언을 포함. `printf` 사용을 위해 `<cstdio>` 포함 필요
  <br><br>- 기타 : Test.h가 include하는 `"Tests.h"`(Test.h:3)도 미존재 — 헤더 체인 전체 빌드 불가
 </details>

#### [P0:Compile include][정훈희][151efc0][Test.h/global/Line:3]
존재하지 않는 헤더 Tests.h include로 컴파일 실패
```cpp
#include <iostream>

#include "Tests.h"
```
 <details>
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 18, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `Tests.h`가 저장소에 존재하지 않음. Test.h를 직접 또는 간접 포함하는 모든 TU가 빌드 불가
  <br><br>- 의견 : `Tests.h`가 필요하다면 파일을 생성하거나 올바른 헤더 경로로 수정, 불필요하면 제거
  <br><br>- 기타 : Test.cpp의 `#include "Huns.h"` 문제(Test.cpp:1)와 병행 — 전체 빌드 블로킹
 </details>

## P2:Medium - 2026/04/19

#### [P2:Return type mismatch][정훈희][1a9a7d9][Test.cpp/TEST()/Line:14]
int TEST()에서 return true 반환 — 의미 불명확
```cpp
int TEST()
{
	// ...
	return true;  // bool→int 암묵 변환(1), 의미 불명확
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 5, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `void TEST()` → `int TEST()`로 반환 타입 변경 시 기존 `return true;` 구문이 잔존. `true`는 int로 암묵 변환(1)되어 컴파일은 통과하지만 반환 의미(성공/실패, 에러코드 등)가 불명확. 함수 목적이 void였다면 반환값 자체 제거가 적절
  <br><br>- 의견 : 반환 목적 명확화 → `return 0;`(정상) / `return -1;`(에러) / 또는 `void`로 복구 후 `return;`으로 변경
  <br><br>- 기타 : 컴파일 블로킹 P0 이슈 해결 후 추가 확인 필요
 </details>
