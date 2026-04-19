## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][f625d50a][Test.cpp/main()/Line:23]
[원인] pM nullptr 역참조 런타임 크래시
```
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
[해결] nullptr 역참조 라인 제거
```
int* pM = nullptr;

printf("T2 %d.\n ", 123);
```
 <details>
  <summary>상태 : [해결] , 위험 : 88, 횟수 : 3, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `main()` 함수에서 `pM`을 `nullptr`로 초기화한 직후 체크 없이 역참조. 프로그램 진입점에서 즉시 크래시 발생. `151efc0` 커밋부터 존재하는 이슈.
  <br><br>- 의견 : `pM` 역참조 전 nullptr 체크 추가 또는 유효한 포인터 할당 후 사용.
  <br><br>- 기타 : `main()` 내 `*pP`(미선언)도 유사한 역참조 문제 존재.
 </details>
 - 사유 : 커밋 3136b89에서 `printf("T1 %d.\n ", *pM);` 라인 삭제로 해결
