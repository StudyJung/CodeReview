## P2:Medium - 2026/04/19

#### [P2:Dormant crash][정훈희][17d38f8][Test.cpp/TEST()/Line:5-7]
`TEST()` 의 nullptr 역참조가 범위 내 주석 해제(896f4c5) 로 활성화 → 재주석(17d38f8) 봉합. 선언·주석 라인 잔존으로 재활성 리스크
``` 문제 코드
int TEST()
{
	int* pT = nullptr;

	//printf("T4 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 45, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : HEAD 에서는 주석 상태라 크래시 미발생. 그러나 `//` 두 문자만 제거하면 `pT` 가 `nullptr` 그대로 `printf` 가변 인자로 역참조되어 즉시 SIGSEGV. 선행 최신{$Output}(1776588202) 의 P0 이 RV2/RV5 관점에서 재활성 잠복 리스크로 강등되어 유지
  <br><br>- 의견 : 미사용 포인터 선언과 주석 라인 모두 삭제. 샘플 의도라면 `int val = 0; printf("T4 %d.\n ", val);` 로 대체
  <br><br>- 기타 : `main()` Line:19-21 과 쌍. 하나의 무의미 커밋(ccc) 이 두 P0 를 동시에 심었던 구조적 취약이 그대로 노출됨
 </details>

#### [P2:Dormant crash][정훈희][17d38f8][Test.cpp/main()/Line:19-21]
`main()` 의 nullptr 역참조가 범위 내 주석 해제(896f4c5) 로 활성화 → 재주석(17d38f8) 봉합. 재활성 리스크
``` 문제 코드
int main()
{
	int* pM = nullptr;

	//printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [미결] , 위험 : 45, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : TEST() Line:5-7 과 동일 구조. HEAD 비활성. 주석 한 번만 풀리면 엔트리 포인트 진입 직후 크래시
  <br><br>- 의견 : 포인터 선언과 주석 라인을 모두 삭제. 포인터 의도가 있으면 유효 지역 변수 주소로 초기화 후 nullptr 가드 추가
  <br><br>- 기타 : TEST() Line:5-7 과 동시 수정 권장. RV6 의 플레이/재화 영역은 아니지만 엔트리 포인트 크래시 잠복이라는 측면에서 계속 추적
 </details>

#### [P2:Undefined identifier][정훈희][896f4c5][Test.cpp/TEST()/Line:11]
`TEST()` dead branch 내 미선언 식별자 `*p5`
``` 문제 코드
if(  false)
{
    printf("T5 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `if(false)` 내부라 실행 경로는 차단되지만 대부분 컴파일러가 파싱·선언 체크를 수행해 빌드 차단 가능
  <br><br>- 의견 : `if(false)` 블록 전체 제거. 코드베이스에 dead code 를 남기지 않음
  <br><br>- 기타 : `pP` 와 동일 계열의 미선언 식별자 패턴
 </details>

## P3:Low - 2026/04/19

#### [P3:Namespace pollution][정훈희][151efc0][Test.h/global/Line:5]
헤더에서 `using namespace std;` — 모든 포함 TU 의 전역 네임스페이스 오염
``` 문제 코드
#include "Tests.h"

using namespace std;
```
 <details>
  <summary>상태 : [미결] , 위험 : 25, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 헤더 포함처마다 전역에 `std` 가 투입되어 심볼 충돌, 암묵 변환, ADL 혼동 유발 가능
  <br><br>- 의견 : 헤더에서 제거. 필요 시 cpp 내부 국소 스코프에서만 사용
  <br><br>- 기타 : 공통 C++ 가이드라인 위반
 </details>

## P2:Medium - 2026/04/19

#### [P2:Undefined identifier][정훈희][896f4c5][Test.cpp/main()/Line:25]
`main()`에서 선언되지 않은 `pP`를 역참조 — 컴파일 에러 또는 의도치 않은 전역 의존
``` 문제 코드
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 55, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`는 현재 파일 어디에도 선언되어 있지 않음. 엄격 빌드에서는 컴파일 에러. 빌드를 통과한다면 알 수 없는 주소를 역참조하는 더 큰 위험
  <br><br>- 의견 : 라인 삭제가 1순위. 반드시 필요하다면 `int nP = 0; int* pP = &nP; printf("T3 %d.\n ", *pP);`로 선언 후 사용
  <br><br>- 기타 : 개발자 노트를 그대로 커밋한 흔적으로 보임. 동일 파일 `p5`(Line:11)와 같은 계열의 문제
 </details>

#### [P2:Dead code identifier][정훈희][896f4c5][Test.cpp/TEST()/Line:11]
`TEST()`의 `if(false)` dead branch 내 미선언 식별자 `p5` — 컴파일러에 따라 에러
``` 문제 코드
if(  false)
{
    printf("T5 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `p5`는 선언되지 않은 식별자. `if(false)` 내부라 실행은 안 되지만, 일부 컴파일러(특히 템플릿 인스턴스화 경로나 `-fsyntax-only`)는 dead branch도 파싱·검사하여 에러 발생 가능
  <br><br>- 의견 : `if(false)` 블록 전체 제거. dead code를 코드베이스에 남기지 않는 것이 원칙
  <br><br>- 기타 : 코드 정리 미흡의 흔적
 </details>

## P2:Medium - 2026/04/19

#### [P2:Undefined identifier][정훈희][896f4c5][Test.cpp/main()/Line:25]
`main()`에서 선언되지 않은 `pP`를 역참조 — 컴파일 에러 또는 의도치 않은 전역 의존
``` 문제 코드
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 55, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`는 현재 파일 어디에도 선언되어 있지 않음. 엄격 빌드에서는 컴파일 에러. 빌드를 통과한다면 알 수 없는 주소를 역참조하는 더 큰 위험
  <br><br>- 의견 : 라인 삭제가 1순위. 반드시 필요하다면 `int nP = 0; int* pP = &nP; printf("T3 %d.\n ", *pP);`로 선언 후 사용
  <br><br>- 기타 : 개발자 노트를 그대로 커밋한 흔적으로 보임. 동일 파일 `p5`(Line:11)와 같은 계열의 문제
 </details>

#### [P2:Dead code identifier][정훈희][896f4c5][Test.cpp/TEST()/Line:11]
`TEST()`의 `if(false)` dead branch 내 미선언 식별자 `p5` — 컴파일러에 따라 에러
``` 문제 코드
if(  false)
{
    printf("T5 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `p5`는 선언되지 않은 식별자. `if(false)` 내부라 실행은 안 되지만, 일부 컴파일러(특히 템플릿 인스턴스화 경로나 `-fsyntax-only`)는 dead branch도 파싱·검사하여 에러 발생 가능
  <br><br>- 의견 : `if(false)` 블록 전체 제거. dead code를 코드베이스에 남기지 않는 것이 원칙
  <br><br>- 기타 : 코드 정리 미흡의 흔적
 </details>

## P2:Medium - 2026/04/19

#### [P2:Undefined identifier][정훈희][896f4c5][Test.cpp/main()/Line:25]
`main()`에서 선언되지 않은 `pP`를 역참조 — 컴파일 에러 또는 의도치 않은 전역 의존
``` 문제 코드
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 55, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`는 현재 파일 어디에도 선언되어 있지 않음. 엄격 빌드에서는 컴파일 에러. 빌드를 통과한다면 알 수 없는 주소를 역참조하는 더 큰 위험
  <br><br>- 의견 : 라인 삭제가 1순위. 반드시 필요하다면 `int nP = 0; int* pP = &nP; printf("T3 %d.\n ", *pP);`로 선언 후 사용
  <br><br>- 기타 : 개발자 노트를 그대로 커밋한 흔적으로 보임. 동일 파일 `p5`(Line:11)와 같은 계열의 문제
 </details>

#### [P2:Dead code identifier][정훈희][896f4c5][Test.cpp/TEST()/Line:11]
`TEST()`의 `if(false)` dead branch 내 미선언 식별자 `p5` — 컴파일러에 따라 에러
``` 문제 코드
if(  false)
{
    printf("T5 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `p5`는 선언되지 않은 식별자. `if(false)` 내부라 실행은 안 되지만, 일부 컴파일러(특히 템플릿 인스턴스화 경로나 `-fsyntax-only`)는 dead branch도 파싱·검사하여 에러 발생 가능
  <br><br>- 의견 : `if(false)` 블록 전체 제거. dead code를 코드베이스에 남기지 않는 것이 원칙
  <br><br>- 기타 : 코드 정리 미흡의 흔적
 </details>
