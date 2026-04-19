
#### [P0:Crash nullptr][정훈희][1a9a7d9][Test.cpp/main()/Line:19-21]
pM nullptr 역참조 크래시
```cpp
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [해결] , 위험 : 99, 횟수 : 9, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pM`이 `nullptr`로 초기화된 직후 `*pM`으로 역참조하여 `main()` 진입 즉시 크래시 발생. 실제 실행 경로이며 회피 불가. Huns02 이전부터 존재한 버그로, 1a9a7d9에서 변수명만 `pT`→`pM`으로 변경됨
  <br><br>- 의견 : `pM`에 유효한 메모리를 할당하거나, 출력 목적이라면 정수 변수 `int nM = 0;`으로 변경
  <br><br>- 기타 : Line:25 `*pP` 미선언과 병행 — main() 전체 컴파일/런타임 이중 차단 상태
 </details>
 - 사유 : 일단 제외
