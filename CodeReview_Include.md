# CodeReview_Include.md

## P1:High - 2026/04/19

#### [P1:Crash nullptr][정훈희][c3dcc12][Test.cpp/TEST()/Line:12]
[원인] pT nullptr 역참조 크래시
```
int* pT = nullptr;

printf("T5 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : TEST 함수에서 `pT`가 `nullptr`로 초기화된 직후 `*pT`로 역참조하여 런타임 크래시가 발생한다. c3dcc12 "dd" 커밋에서 f625d50이 제거했던 printf가 재도입되어 회귀가 생겼다.
  <br><br>- 의견 : 역참조 전 `if (pT != nullptr)` 가드 추가 또는 해당 printf 제거
  <br><br>- 기타 : 회귀 이슈(f625d50 해결 → c3dcc12 재도입). 동일 패턴의 main() `*pM` 이슈 동반 발생. RV7에 따라 test/ 하위 코드이므로 중요도 하향(P0→P1)
 </details>

#### [P1:Crash nullptr][정훈희][f625d50][Test.cpp/main()/Line:21]
[원인] pM nullptr 역참조 크래시
```
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [미결] , 위험 : 85, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : main 함수에서 `pM`이 `nullptr`로 초기화된 직후 `*pM`로 역참조하여 런타임 크래시가 발생한다. f625d50에서 도입되었으며 이후 c3dcc12까지 유지되었다.
  <br><br>- 의견 : 역참조 전 `if (pM != nullptr)` 가드 추가 또는 해당 printf 제거
  <br><br>- 기타 : TEST() `*pT`와 동일 패턴의 이슈. RV7에 따라 test/ 하위 코드이므로 중요도 하향(P0→P1)
 </details>

#### [P1:Undefined symbol][정훈희][f625d50][Test.cpp/TEST()/Line:9]
[원인] 미선언 심볼 p5 역참조
```
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 80, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `p5` 식별자가 어디에도 선언되어 있지 않아 컴파일 에러가 발생한다. `if(false)` 블록 안에 있어 런타임 경로로는 진입하지 않지만 컴파일러는 해당 문장을 여전히 파싱/심볼 해석을 수행하므로 빌드가 실패한다.
  <br><br>- 의견 : `p5` 선언 추가 또는 해당 블록 전체 삭제
  <br><br>- 기타 : f625d50 커밋에서 라벨만 T5→T4로 변경되었을 뿐 미선언 심볼 문제는 유지됨. RV7에 따라 test/ 하위 코드이므로 중요도 하향(P0→P1)
 </details>

#### [P1:Undefined symbol][정훈희][151efc0][Test.cpp/main()/Line:25]
[원인] 미선언 심볼 pP 역참조
```
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 80, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP` 식별자가 어디에도 선언되어 있지 않아 컴파일 에러가 발생한다. 초기 커밋부터 존재했고 test2 이후 범위에서도 제거되지 않아 HEAD에도 그대로 남아있다.
  <br><br>- 의견 : `pP` 선언 추가 또는 해당 printf 라인 삭제
  <br><br>- 기타 : 스코프(test2..HEAD) 내부 커밋에서 직접 수정은 없으나 HEAD 소스 기준 이슈이므로 보고(RV2). RV7에 따라 test/ 하위 코드이므로 중요도 하향(P0→P1)
 </details>
