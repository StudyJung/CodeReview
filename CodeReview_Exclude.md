## P0:Critical - 2026/04/19

#### [P0:TEST nullptr][정훈희][c3dcc12][Test.cpp/TEST()/Line:5-12]
[원인] pT nullptr 초기화 후 무조건 역참조
```cpp
int* pT = nullptr;

if(  false)
{
	printf("T4 %d.\n ", *p5);
}

printf("T5 %d.\n ", *pT);
```
[추천] 역참조 전 nullptr 체크 추가
```cpp
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
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 후 `if(false)` 블록 외부에서 `printf("T5 %d.\n ", *pT)`를 무조건 실행하여 런타임 크래시 확정. c3dcc12("dd") 커밋에서 해당 printf가 조건 블록 밖으로 이동. 이전 커밋 f625d50의 메시지("pT printf removed")와 실제 diff(추가) 불일치로 추적 혼란 발생. (테스트 코드로 위험도 조정 -9)
  <br><br>- 의견 : `if (pT != nullptr)` 체크 후 역참조하거나, 테스트 의도라면 주석 처리
  <br><br>- 기타 : 동일 nullptr 역참조 패턴이 main()의 pM에도 존재 (연관 이슈 참조)
 </details>
