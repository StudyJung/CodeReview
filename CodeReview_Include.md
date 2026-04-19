## P1:High - 2026/04/19

#### [P1:Crash nullptr][정훈희][c3dcc12][Test.cpp/TEST()/Line:12]
[원인] pT nullptr 역참조 런타임 크래시
```
int* pT = nullptr;

printf("T5 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 70, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `c3dcc12` 커밋에서 `TEST()` 함수 라인 12에 `printf("T5 %d.\n ", *pT);` 도입. `pT`는 `nullptr`로 초기화되어 `*pT` 역참조 시 런타임 크래시. 함수 진입 후 데드코드(Line:7-10) 건너뛰고 처음 만나는 실행 가능한 역참조 지점이므로 T5에서 크래시 확정. T5가 먼저 실행되어 T7 도달 전에 크래시.
  <br><br>- 의견 : `pT` 역참조 전 nullptr 체크 추가 또는 유효한 포인터 할당 후 사용.
  <br><br>- 기타 : T7(Line:14)와 동일 원인. RV4(유사 문제 확인) 및 RV7(테스트 코드) 적용.
 </details>

#### [P1:Crash nullptr][정훈희][151efc0][Test.cpp/main()/Line:23]
[원인] pM nullptr 역참조 런타임 크래시
```
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [미결] , 위험 : 70, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `151efc0` 커밋부터 존재하는 이슈. `main()` 진입 직후 `pM`이 `nullptr`로 초기화되고 라인 23에서 `*pM` 역참조하여 프로그램 즉시 크래시. `TEST()` 호출 없이 `main()` 단독 실행 경로에서도 크래시 발생.
  <br><br>- 의견 : `pM` 역참조 전 nullptr 체크 추가 또는 유효한 포인터 할당 후 사용.
  <br><br>- 기타 : `TEST()` 함수의 T5/T7과 동일 패턴. RV4 및 RV7 적용.
 </details>
