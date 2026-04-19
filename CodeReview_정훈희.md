## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][896f4c5][Test.cpp/TEST()/Line:7]
`TEST()`에서 `nullptr`로 초기화한 `pT`를 `*pT`로 역참조하여 호출 즉시 SIGSEGV
``` 문제 코드
int* pT = nullptr;

printf("T4 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr` 초기값 그대로 유지된 채 `printf`의 가변 인자로 `*pT`가 평가됨. `TEST()`가 호출되는 모든 경로에서 SIGSEGV 발생. `896f4c5 (ccc)` 커밋이 `//printf` 주석을 해제하며 활성화됨
  <br><br>- 의견 : 포인터가 불필요하면 `int nT = 0; printf("T4 %d.\n ", nT);`로 교체. 포인터 경로가 의도라면 유효한 변수 주소(`&val`)로 초기화하고 nullptr 가드 추가
  <br><br>- 기타 : 동일 커밋에서 `main()` Line:21에도 동일 패턴이 함께 활성화됨. 하나의 주석 해제 커밋이 두 개의 P0 크래시를 동시에 심은 구조. 커밋 메시지 "ccc"에 변경 의도가 없어 위험 인지 불가
 </details>

#### [P0:Crash nullptr][정훈희][896f4c5][Test.cpp/main()/Line:21]
`main()`에서 `nullptr`로 초기화한 `pM`을 `*pM`으로 역참조해 프로세스 기동 즉시 SIGSEGV
``` 문제 코드
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pM`을 `nullptr`로 초기화한 직후 `printf` 가변 인자로 `*pM`을 전달. 함수 호출 스택 구성 시점에 역참조가 일어나 엔트리 포인트 진입 직후 크래시
  <br><br>- 의견 : `int nM = 0; printf("T1 %d.\n ", nM);`으로 교체. 포인터 경로 유지 시 유효한 지역 변수 주소로 초기화 후 nullptr 체크 추가
  <br><br>- 기타 : `TEST()` Line:7 이슈와 묶어 동시 수정 권장. 두 이슈 모두 "ccc" 커밋의 주석 해제에 의해 활성화됨
 </details>
