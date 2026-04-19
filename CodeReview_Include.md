## P0:Critical - 2026/04/19

#### [P0:Compile error][정훈희][f625d50][Test.cpp/main()/Line:23]
main pP 미선언 식별자 역참조
```
printf("T3 %d.\n ", *pP);
```
미선언 식별자 제거 또는 선언·초기화 추가
```
int nP = 0;
printf("T3 %d.\n ", nP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 98, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `main()`에서 선언되지 않은 식별자 `pP`를 `*pP`로 역참조. 컴파일 오류로 빌드 자체 실패. 또한 `main()`이 `int` 반환 타입이지만 `return` 문도 없음(C++은 main에 한해 암묵 `return 0` 허용이나 방어적으로 명시 권장)
  <br><br>- 의견 : `pP`를 선언·초기화하거나 해당 라인 제거. 의도가 테스트용 크래시라면 명확한 변수와 초기화값을 사용하고 주석으로 표시
  <br><br>- 기타 : TEST()의 `*p5`(dead code 내부)와 동일 패턴으로 미선언 식별자 역참조가 반복됨. 코드 전반 식별자 선언 검사 필요
 </details>

#### [P0:Compile error][정훈희][f625d50][Test.cpp/TEST()/Line:7-10]
TEST p5 미선언 식별자 역참조
```
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
미선언 식별자 제거 또는 dead code 블록 제거
```
// dead code 제거
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 2, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `if(false)` 내부의 dead code 블록에서 선언되지 않은 식별자 `p5`를 `*p5`로 역참조. 조건이 항상 거짓이라 런타임 진입은 없으나, 컴파일 단계 이름 탐색에서 오류 발생(빌드 실패). 커밋 387a3ff에서 문자열 리터럴만 'T5'→'T4'로 바뀌었을 뿐 미선언 식별자 이슈는 잔존
  <br><br>- 의견 : dead code 블록 전체 제거 또는 `p5`를 올바르게 선언. 테스트 샘플 용도라면 `#if 0 / #endif`로 감싸 식별자 조회 자체를 차단
  <br><br>- 기타 : `main()`의 `*pP`와 동일한 미선언 역참조 패턴. HEAD 소스에 잔존
 </details>
