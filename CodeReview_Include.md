
## P1:High - 2026/04/19

#### [P1:Main nullptr][정훈희][f625d50][Test.cpp/main()/Line:19-21]
[원인] pM nullptr 초기화 직후 무조건 역참조
```cpp
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
[추천] 역참조 전 nullptr 체크 추가
```cpp
int* pM = nullptr;

if (pM != nullptr)
{
	printf("T1 %d.\n ", *pM);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pM`이 `nullptr`로 초기화된 직후 `printf("T1 %d.\n ", *pM)` 역참조로 런타임 크래시 확정. f625d50 커밋에서 추가됨. 이전에는 해당 줄이 주석 처리되어 있었으나 주석 해제 후 nullptr 체크 없이 역참조. (테스트 코드로 위험도 조정 -9)
  <br><br>- 의견 : `if (pM != nullptr)` 체크 후 역참조하거나, 테스트 의도라면 주석 복원
  <br><br>- 기타 : TEST()의 pT nullptr 역참조와 동일 패턴. c3dcc12 이후 동일 파일 내 P0 크래시 2건 확인
 </details>

## P2:Medium - 2026/04/19

#### [P2:Header missing][정훈희][151efc0][Test.cpp/main()/Line:1,25]
[원인] Huns.h git 미추적으로 pP 출처 불명
```cpp
#include "Huns.h"

// ...
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `Huns.h`가 git에 추적되지 않아 `pP`의 선언/초기화를 확인할 수 없음. 로컬 환경에서만 빌드 가능하며 CI/CD 또는 타 개발자 환경에서 컴파일 실패 위험. `pP`가 nullptr일 경우 P0 크래시로 상승 가능.
  <br><br>- 의견 : `Huns.h`를 git에 추가하거나, `pP` 선언을 Test.cpp 내부로 이동
  <br><br>- 기타 : `p5` 변수도 동일 헤더 의존. `if(false)` 내부이므로 현재는 실행 안 됨
 </details>

## P4:Minimal - 2026/04/19

#### [P4:Dead code][정훈희][151efc0][Test.cpp/TEST()/Line:7-10]
[원인] if(false) 블록 dead code 및 불필요 공백
```cpp
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 04, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `if(false)` 조건으로 블록 내부는 절대 실행되지 않는 dead code. `if(  false)` 과도한 공백도 컨벤션 위반. `*p5` 참조가 포함되어 있어 Huns.h 없이 컴파일 불가.
  <br><br>- 의견 : dead code 제거 또는 테스트 의도라면 `#ifdef _DEBUG` 조건부 컴파일로 변경
 </details>
