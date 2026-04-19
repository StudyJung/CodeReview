## P1:High - 2026/04/19

#### [P1:Crash nullptr][정훈희][c3dcc12][Test.cpp/TEST()/Line:12]
[원인] pT nullptr 역참조 런타임 크래시
```
int* pT = nullptr;

printf("T5 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 70, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 후 라인 12에서 `*pT` 역참조로 런타임 크래시 발생. `c3dcc12` 커밋에서 도입. T7(Line:14) 신규 추가로 동일 함수 내 크래시 지점 2개가 됨. T5가 먼저 실행되어 T7 도달 전에 크래시.
  <br><br>- 의견 : nullptr 체크 또는 유효한 포인터 할당 필요.
  <br><br>- 기타 : T7(Line:14)와 동일 원인. RV4(유사 문제 확인) 및 RV7(테스트 코드) 적용.
 </details>

#### [P1:Crash nullptr][정훈희][151efc0][Test.cpp/main()/Line:23]
[원인] pM nullptr 역참조 런타임 크래시
```
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [미결] , 위험 : 70, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pM`이 `nullptr`로 초기화된 직후 라인 23에서 `*pM` 역참조로 런타임 크래시. `main()` 진입 후 즉시 크래시. `151efc08`(Add files via upload) 커밋부터 존재.
  <br><br>- 의견 : nullptr 체크 또는 유효한 포인터 할당 필요.
  <br><br>- 기타 : TEST() 함수의 T5/T7과 동일 패턴. RV4 및 RV7 적용.
 </details>
