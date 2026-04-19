## P2:Medium - 2026/04/19

#### [P2:Compile undef][정훈희][151efc0][Test.cpp/main()/Line:27]
[원인] 미정의 변수 pP 역참조 컴파일 오류
```
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 65, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 선언되지 않은 변수 `pP`를 `*pP`로 역참조. 컴파일 오류로 빌드 불가. `Huns.h` 등 포함 헤더에도 선언 미확인. `151efc08` 커밋부터 존재.
  <br><br>- 의견 : `pP` 선언 추가(`int* pP = nullptr;` 등) 또는 정의된 변수 사용.
  <br><br>- 기타 : T4(Line:9)의 `p5`와 동일 패턴. RV4 및 RV7 적용.
 </details>

## P3:Low - 2026/04/19

#### [P3:DeadCode undef][정훈희][f625d50][Test.cpp/TEST()/Line:7-10]
[원인] 데드코드 내 미정의 변수 p5 컴파일 오류
```
if(  false)
{
	printf("T4 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `if(false)` 데드코드 블록 내에서 선언되지 않은 변수 `p5` 역참조. 실행되지 않지만 C++ 컴파일 단계에서 오류 발생. `if(  false)` 공백 중복도 존재. `f625d50` 커밋에서 도입.
  <br><br>- 의견 : `p5` 선언 추가 또는 데드코드 블록 전체 제거. 공백 정리.
  <br><br>- 기타 : T3(Line:27)의 `pP`와 동일 패턴. 데드코드 자체도 정리 대상. RV7 적용.
 </details>
