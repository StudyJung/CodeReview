## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][c3dcc12b][Test.cpp/TEST()/Line:12]
[원인] pT nullptr 역참조 런타임 크래시
```
int* pT = nullptr;

printf("T5 %d.\n ", *pT);
```
[추천] nullptr 체크 후 역참조
```
int* pT = nullptr;

if (pT != nullptr)
{
	printf("T5 %d.\n ", *pT);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 90, 횟수 : 3, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `c3dcc12b` 커밋에서 `TEST()` 함수 라인 12에 `printf("T5 %d.\n ", *pT);` 도입. `pT`는 `nullptr`로 초기화되어 `*pT` 역참조 시 런타임 크래시. 함수 진입 후 데드코드(Line:7-10) 건너뛰고 처음 만나는 실행 가능한 역참조 지점이므로 T5에서 크래시 확정.
  <br><br>- 의견 : 역참조 전 nullptr 체크 추가 또는 유효한 포인터 할당 후 사용. Line:14(T7)와 동일 패턴으로 함께 수정 필요.
  <br><br>- 기타 : T7(Line:14)와 동일 원인. Line:27(`*pP`, 미선언)도 유사한 역참조 문제 존재.
 </details>

#### [P0:Crash nullptr][정훈희][f625d50a][Test.cpp/main()/Line:23]
[원인] pM nullptr 역참조 런타임 크래시
```
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
[추천] nullptr 체크 후 역참조
```
int* pM = nullptr;

if (pM != nullptr)
{
	printf("T1 %d.\n ", *pM);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 88, 횟수 : 3, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `main()` 함수에서 `pM`을 `nullptr`로 초기화한 직후 체크 없이 역참조. 프로그램 진입점에서 즉시 크래시 발생. `151efc0` 커밋부터 존재하는 이슈.
  <br><br>- 의견 : `pM` 역참조 전 nullptr 체크 추가 또는 유효한 포인터 할당 후 사용. `TEST()` 함수의 T5/T7과 동일 패턴.
  <br><br>- 기타 : `main()` 내 Line:27(`*pP`, 미선언)도 유사한 역참조 문제 존재.
 </details>

## P1:High - 2026/04/19

#### [P1:Dead undeclared][정훈희][f625d50a][Test.cpp/TEST()/Line:9]
[원인] 데드코드 내 미선언 변수 p5 컴파일 에러
```
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `if(false)` 데드코드 블록 내 `p5` 미선언 변수 역참조. 런타임 실행은 되지 않으나 대부분의 컴파일러에서 미선언 변수로 인한 컴파일 에러 발생. 이중 공백(`if(  false)`)으로 코드 품질도 낮음.
  <br><br>- 의견 : 데드코드 블록 제거 또는 `p5` 변수 선언 추가 필요. `if(false)` 블록 자체를 삭제하는 것이 코드 정리 측면에서 권장.
  <br><br>- 기타 : Line:27(`*pP`, 미선언)과 동일한 미선언 변수 패턴. 데드코드이므로 런타임 영향은 없으나 컴파일 에러로 빌드 차단.
 </details>
