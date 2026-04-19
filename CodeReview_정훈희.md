## P1:High - 2026/04/19

#### [P1:Crash nullptr][정훈희][896f4c5][Test.cpp/main()/Line:21]
`main()`에서 `nullptr`로 초기화한 `pM`을 `*pM`으로 역참조해 프로세스 기동 즉시 SIGSEGV
``` 문제 코드
int main()
{
	int* pM = nullptr;

	printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pM`을 `nullptr`로 초기화한 직후 `printf` 가변 인자로 `*pM`을 전달. 함수 호출 스택 구성 시점에 역참조가 일어나 엔트리 포인트 진입 직후 크래시. 이전 커밋에서는 주석으로 막혀 있었으나 `896f4c5`가 주석을 해제하며 활성화됨
  <br><br>- 의견 : 포인터가 필요한 로직이 아니라면 `int nM = 0;`으로 바꿔 `printf("T1 %d.\n ", nM);`로 호출. 포인터 경로를 유지해야 한다면 유효한 스택 변수 주소(`&nM`)로 초기화하고 역참조 전에 `nullptr` 체크 추가
  <br><br>- 기타 : 동일 커밋에서 `TEST()` 내부에도 같은 패턴(`*pT`)이 함께 되살아남. 하나의 "주석 해제" 커밋이 두 개의 P1 크래시를 동시에 심은 구조이므로 rollback 또는 일괄 수정 필요. `test/` 디렉터리 하위 파일이지만 `main()` 엔트리를 포함하므로 실행 시 실제 프로세스 크래시로 이어짐
 </details>

#### [P1:Crash nullptr][정훈희][896f4c5][Test.cpp/TEST()/Line:7]
`TEST()`에서 `nullptr`로 초기화한 `pT`를 `*pT`로 역참조하여 호출 즉시 크래시
``` 문제 코드
int TEST()
{
	int* pT = nullptr;

	printf("T4 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 88, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`이 `nullptr` 초기값 그대로 유지된 채 `*pT`가 `printf`의 가변 인자로 평가됨. `TEST()`가 호출되는 모든 경로에서 SIGSEGV 발생
  <br><br>- 의견 : 포인터 필요 없는 코드이므로 `int nT = 0; printf("T4 %d.\n ", nT);`로 교체. 포인터 경로가 의도라면 유효한 지역/전역 변수 주소로 초기화 후 nullptr 가드 추가
  <br><br>- 기타 : 주석(`//printf`) 해제 역행 커밋(`896f4c5`, 메시지 "ccc") 하나가 원인. 커밋 메시지에 변경 사유/의도가 전혀 없음 — 위험 코드 재활성화 시 사유 기재 컨벤션 필요. 같은 파일의 `main()` Line:21 이슈와 묶어 동시 수정 권장
 </details>
