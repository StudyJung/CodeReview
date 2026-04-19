## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][f625d50][Test.cpp/TEST()/Line:5-12]
TEST pT nullptr 역참조 크래시
```
int* pT = nullptr;

if(  false)
{
	printf("T4 %d.\n ", *p5);
}

printf("T5 %d.\n ", *pT);
```
포인터 역참조 전 nullptr 체크 추가
```
int* pT = nullptr;

if(  false)
{
	printf("T4 %d.\n ", *p5);
}

if (pT != nullptr)
{
	printf("T5 %d.\n ", *pT);
}
```
 <details>
  <summary>상태 : [해결] , 위험 : 99, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 뒤 `*pT` 역참조로 `printf`에 전달되어 런타임 크래시 발생. 이 라인은 커밋 f625d50에서 '해결' 이력이 있었으나 이후 다시 동일 라인이 재도입됨(회귀)
  <br><br>- 의견 : 역참조 전 `if (pT != nullptr)` 가드 추가. 테스트 의도가 '크래시 재현' 이라면 라인 위에 주석으로 의도 명시하고 프로덕션 빌드에서 배제
  <br><br>- 기타 : `main()`의 `*pM`과 동일 패턴 이중 발생. nullptr 초기화 포인터의 역참조를 전수 검사 필요
 </details>
 - 사유 : 커밋 387a3ff(cc)에서 `printf("T5 %d.\n ", *pT);` 라인이 제거되어 HEAD 소스에서 `*pT` 역참조가 사라짐. `pT` 변수 자체는 TEST()/Line:5에 선언되어 있으나 미사용 상태로 잔존
