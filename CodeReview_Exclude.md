# CodeReview_Exclude.md
#### [P1:Crash nullptr][정훈희][c3dcc12][Test.cpp/TEST()/Line:12]
[원인] pT nullptr 역참조 크래시
```
int* pT = nullptr;

printf("T5 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : TEST 함수에서 `pT`가 `nullptr`로 초기화된 직후 `*pT`로 역참조하여 런타임 크래시가 발생한다. c3dcc12 "dd" 커밋에서 f625d50이 제거했던 printf가 재도입되어 회귀가 생겼다.
  <br><br>- 의견 : 역참조 전 `if (pT != nullptr)` 가드 추가 또는 해당 printf 제거
  <br><br>- 기타 : 회귀 이슈(f625d50 해결 → c3dcc12 재도입). 동일 패턴의 main() `*pM` 이슈 동반 발생. RV7에 따라 test/ 하위 코드이므로 중요도 하향(P0→P1)
 </details>