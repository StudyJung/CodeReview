## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][f625d50][Test.cpp/main()/Line:19-21]
main pM nullptr 역참조 크래시
```
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
  <summary>상태 : [미결] , 위험 : 99, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 뒤 `*pT` 역참조로 `printf`에 전달되어 런타임 크래시 발생. 이 라인은 커밋 f625d50에서 '해결' 이력이 있었으나 이후 다시 동일 라인이 재도입됨(회귀)
  <br><br>- 의견 : 역참조 전 `if (pT != nullptr)` 가드 추가. 테스트 의도가 '크래시 재현' 이라면 라인 위에 주석으로 의도 명시하고 프로덕션 빌드에서 배제
  <br><br>- 기타 : `main()`의 `*pM`과 동일 패턴 이중 발생. nullptr 초기화 포인터의 역참조를 전수 검사 필요
 </details>

#### [P0:Compile error][정훈희][f625d50][Test.cpp/main()/Line:25]
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
  <summary>상태 : [미결] , 위험 : 98, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `main()`에서 선언되지 않은 식별자 `pP`를 `*pP`로 역참조. 컴파일 오류로 빌드 자체 실패. 또한 `main()`이 `int` 반환 타입이지만 `return` 문도 없음(C++은 main에 한해 암묵 `return 0` 허용이나 방어적으로 명시 권장)
  <br><br>- 의견 : `pP`를 선언·초기화하거나 해당 라인 제거. 의도가 테스트용 크래시라면 명확한 변수와 초기화값을 사용하고 주석으로 표시
  <br><br>- 기타 : TEST()의 `*p5`(dead code 내부)와 동일 패턴으로 미선언 식별자 역참조가 반복됨. 코드 전반 식별자 선언 검사 필요
 </details>

#### [P0:Compile error][정훈희][f625d50][Test.cpp/TEST()/Line:7-9]
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
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `if(false)` 내부의 dead code 블록에서 선언되지 않은 식별자 `p5`를 `*p5`로 역참조. 조건이 항상 거짓이라 런타임 진입은 없으나, 컴파일 단계 이름 탐색에서 오류 발생(빌드 실패)
  <br><br>- 의견 : dead code 블록 전체 제거 또는 `p5`를 올바르게 선언. 테스트 샘플 용도라면 `#if 0 / #endif`로 감싸 식별자 조회 자체를 차단
  <br><br>- 기타 : `main()`의 `*pP`와 동일한 미선언 역참조 패턴. 이 커밋(f625d50) 범위에서 추가된 것은 아니지만 HEAD 소스에 잔존
 </details>
