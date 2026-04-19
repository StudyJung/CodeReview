#### [P0:Nullptr Crash][정훈희][f123450][Test.cpp/main()/Line:10-20]
역참조 크래시 main nullptr crash 
[이슈 코드]```
int* pM = nullptr;
printf("T1 %d.\n ", *pM);
```
포인터 역참조 전 nullptr 체크 추가
```
int* pM = nullptr;

if (pM != nullptr)
{
	printf("T1 %d.\n ", *pM);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 99, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pM`이 `nullptr`로 초기화된 뒤 곧바로 `*pM` 역참조로 `printf`에 전달되어 런타임 크래시 발생. 커밋 f625d50에서 새로 추가된 라인으로, 이전에 해결되었던 동일 패턴(TEST의 pT) 옆에 동일한 실수가 재도입됨
  <br><br>- 의견 : 포인터 역참조 전 nullptr 가드를 두거나, 역참조가 불필요하면 `*pM`을 제거하고 `pM` 자체 또는 상수값을 출력하도록 변경. 테스트 코드라면 의도가 '크래시 시뮬레이션'인지 댓글로 명시 필요
  <br><br>- 기타 : 동일 파일 내 `TEST()`의 `*pT` 역참조와 완전 동일 패턴. 전체적인 nullptr 역참조 누락 점검 필요
 </details>
