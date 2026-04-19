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
