## P0:Critical - 2026/04/19

#### [P0:Crash undeclared][Hns][151efc08][Test.cpp/main()/Line:27]
[원인] 미선언 변수 pP 역참조 컴파일 에러
```
printf("T3 %d.\n ", *pP);
```
[추천] pP 선언 또는 제거
```
// pP 사용 제거 또는 유효한 포인터 변수 선언 후 사용
int* pP = nullptr;
if (pP != nullptr)
{
	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`가 `main()` 스코프에서 선언되지 않은 변수로 역참조 시도. 컴파일 에러로 빌드 자체가 불가하며 런타임 크래시 전 빌드 단계에서 차단.
  <br><br>- 의견 : `pP` 변수 선언 추가 또는 해당 라인 제거 필요.
  <br><br>- 기타 : Line:9(`*p5`, 미선언, if(false) 데드코드)도 동일한 미선언 패턴 존재.
 </details>
