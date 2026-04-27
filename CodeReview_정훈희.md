# CodeReview_정훈희.md
- "작은 버그 하나가 시스템 전체를 멈춘다. 오늘 발견한 것이 내일의 장애를 막는다." — 작자 미상

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **갱신일** | 2026/04/27 |
| **미결** | 1개 |
| **해결** | 0개 |

| 등급 | 건수 | 설명 |
| :--- | :--- | :--- |
| **P0:Critical** | 0개 |  |
| **P1:High** | 1개 | nullptr 역참조 크래시 |
| **합계** | 1개 |  |

## P1:High - 2026/04/27

#### [P1:Crash nullptr][6e0b5ae/정훈희][Test.cpp/TEST()/Line:5-16]
[원인] printf nullptr 역참조 크래시
```
int* pT = nullptr;
생략...

printf("T8 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 68, 횟수 : 1, 추적 : 2026/04/27 - 2026/04/27</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 후 유효한 주소 할당 없이 `printf("T8 %d.\n ", *pT)`에서 역참조되어 실행 시 즉시 Access Violation 크래시 발생. 이번 커밋(6e0b5ae)에서 신규 추가된 라인.
  <br><br>- 의견 : `pT`에 유효한 `int` 변수의 주소를 할당하거나, `if (pT != nullptr)` 가드 추가. T5·T7 라인도 동일 패턴으로 존재하므로 함수 전체 재검토 권장.
  <br><br>- 기타 : `TEST()` 함수는 `main()`에서 호출되지 않는 dead code. `test/` 디렉토리 내 테스트 파일(RV5 적용). RV2(Crash 높게)와 RV5(Test 낮게) 상쇄로 P1 조정.
 </details>