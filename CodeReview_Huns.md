# CodeReview_Huns.md
- "오늘 고친 한 줄의 코드가 내일의 장애를 막는다." - 작자 미상

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **작업자** | Huns |
| **기준 Include** | CodeReview_Include.md |
| **Period** | 2026/04/19 22:09:25 - 2026/04/20 08:25:39 |
| **Model(Effort)** | claude-opus-4-7 (--effort max) |
| **Tools** | '/check' |

| 등급 | 건수 | 설명 |
| :--- | :--- | :--- |
| **P0:Critical** | 1개 | nullptr 역참조 회귀 |
| **P1:High** | 0개 | - |
| **합계** | 1개 |   |

## P0:Critical - 2026/04/19

#### [P0:Crash regression][Huns][b41368f][Test.cpp/TEST()/Line:14]
[원인] T7 nullptr 역참조 라인 재삽입 회귀
```cpp
	printf("T5 %d.\n ", *pT);

printf("T7 %d.\n ", *pT);
```
[추천] 라인 제거 또는 유효 포인터 할당
```cpp
	printf("T5 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 99, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : 커밋 `b41368f`에서 `printf("T7 %d.\n ", *pT);` 라인을 다시 추가하여 `nullptr` 역참조 크래시 회귀. 이전에 커밋 `3136b89`에서 제거되었던 코드가 재도입됨. 들여쓰기도 누락되어 코드 스타일도 깨짐. Exclude(`2722022`)에서 동일 패턴의 기존 제외 항목이 삭제되면서 재발.
  <br><br>- 의견 : 해당 라인 삭제 또는 역참조 전 `nullptr` 체크 추가. Exclude 해제와 함께 재도입된 회귀이므로 근본 원인 수정 필요.
  <br><br>- 기타 : `Test.cpp` Line 12의 T5 `*pT` 역참조(동일 `pT`)와 중복된 사이드 이펙트. Line 12 T5에서 이미 크래시하므로 도달 불가이나 잠재 크래시 위험 동일.
 </details>
