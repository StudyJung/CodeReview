#### [P1:Crash nullptr][정훈희][ee1e1aa][Test.cpp/TEST()/Line:14]
[원인] pT nullptr 역참조 런타임 크래시
```
int* pT = nullptr;

printf("T7 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 75, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 후 라인 14에서 `*pT` 역참조로 런타임 크래시 발생. `ee1e1aa` 커밋에서 신규 추가된 `printf("T7 %d.\n ", *pT);`. 동일 함수 내 `Line:12`(T5)와 동일한 패턴이며, 실행 시 T5보다 후에 크래시.
  <br><br>- 의견 : 역참조 전 nullptr 체크 추가 또는 `pT`에 유효한 포인터 할당 후 사용.
  <br><br>- 기타 : T5(Line:12)와 동일 원인. RV7 적용(테스트 코드).
 </details>
