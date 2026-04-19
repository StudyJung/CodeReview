# CodeReview_Minority.md

## P2:Medium - 2026/04/19

#### [P2:Undefined identifier][정훈희][896f4c5][Test.cpp/main()/Line:25]
`main()`에서 선언되지 않은 식별자 `pP`를 역참조 — 컴파일 실패 또는 의도치 않은 전역 의존
``` 문제 코드
	printf("T2 %d.\n ", 123);

	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 60, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pP`는 현재 파일과 `Test.h`(`#include <iostream>`, `Tests.h` 포함) 어디에서도 선언되어 있지 않음. 엄격한 빌드에서는 `undeclared identifier` 컴파일 에러, 외부 링크로 뚫린다면 알 수 없는 전역 주소를 역참조하는 더 큰 위험
  <br><br>- 의견 : 라인 삭제가 1순위. 반드시 필요하다면 지역 `int* pP = &nSome;`로 선언하고 역참조 전에 nullptr 체크. 전역 의존이 의도라면 헤더에 선언 노출
  <br><br>- 기타 : 현재 변경된 diff에는 포함되지 않았지만 HEAD 상태에서 살아있는 코드이므로 RV2(HEAD 기준 이슈 확인)에 의해 포함. 함수 바로 위 미정의 `p5`(Line:11)와 같은 계열의 문제 — 개발자 노트를 그대로 커밋한 흔적으로 보임
 </details>

#### [P2:Return missing][정훈희][896f4c5][Test.cpp/main()/Line:17-26]
`int main()`에 명시적 `return`이 없음. 또한 `TEST()`는 `int` 반환에 `return true;`로 반환 규약 전반이 흐트러짐
``` 문제 코드
	printf("T3 %d.\n ", *pP);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 45, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : C++에서 `main`은 예외적으로 묵시 `return 0`이 허용되지만, 프로젝트 컨벤션/정적 분석 관점에서는 항상 명시가 원칙. 현 코드는 `main()`이 실제로는 crash로 종료되기 때문에 반환값이 드러나지 않지만, 크래시 이슈 수정 후에는 즉시 표면화됨
  <br><br>- 의견 : `main()` 마지막에 `return 0;` 추가. 동일 파일 `TEST()` Line:14의 `return true;`도 `return 0;`으로 교체해 반환 타입과 값 타입을 일치
  <br><br>- 기타 : 크래시 2건(P1)이 선행 수정되면 이 이슈가 남아 추후 "왜 실행은 되는데 exit code가 이상한가" 형태의 디버깅 비용으로 전환됨. 선행 수정과 함께 묶어 처리 권장
 </details>
