## P2:Medium - 2026/04/19

#### [P2:Undefined identifier][정훈희][896f4c5][Test.cpp/main()/Line:25]
`main()`에서 선언되지 않은 `pP`를 역참조 — 컴파일 에러 또는 의도치 않은 전역 의존
``` 문제 코드
printf("T3 %d.\n ", *pP);
```
 <details>
  <summary>상태 : [미결] , 위험 : 55, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`는 현재 파일 어디에도 선언되어 있지 않음. 엄격 빌드에서는 컴파일 에러. 빌드를 통과한다면 알 수 없는 주소를 역참조하는 더 큰 위험
  <br><br>- 의견 : 라인 삭제가 1순위. 반드시 필요하다면 `int nP = 0; int* pP = &nP; printf("T3 %d.\n ", *pP);`로 선언 후 사용
  <br><br>- 기타 : 개발자 노트를 그대로 커밋한 흔적으로 보임. 동일 파일 `p5`(Line:11)와 같은 계열의 문제
 </details>

#### [P2:Dead code identifier][정훈희][896f4c5][Test.cpp/TEST()/Line:11]
`TEST()`의 `if(false)` dead branch 내 미선언 식별자 `p5` — 컴파일러에 따라 에러
``` 문제 코드
if(  false)
{
    printf("T5 %d.\n ", *p5);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 35, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `p5`는 선언되지 않은 식별자. `if(false)` 내부라 실행은 안 되지만, 일부 컴파일러(특히 템플릿 인스턴스화 경로나 `-fsyntax-only`)는 dead branch도 파싱·검사하여 에러 발생 가능
  <br><br>- 의견 : `if(false)` 블록 전체 제거. dead code를 코드베이스에 남기지 않는 것이 원칙
  <br><br>- 기타 : 코드 정리 미흡의 흔적
 </details>
