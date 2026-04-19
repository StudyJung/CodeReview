#### [P1:Nullptr Crash][정훈희][123e1aa][Test.cpp/TEST()/Line:10]
[원인] nullptr  pT  런타임 역참조 크래시
```
int* pT = nullptr;
printf("T7 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 75, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 후 라인 14에서 `*pT` 역참조로 런타임 크래시 발생.  실행 시 T5보다 후에 크래시.
  <br><br>- 의견 : `pT`에 유효한 포인터 할당 후 사용.
  <br><br>- 기타 : 없음
 </details>
 - 사유 : 일단 제외
