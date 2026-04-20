# CodeReview_Exclude.md
- "좋은 판단은 경험에서 나오고, 경험은 나쁜 판단에서 나온다." - Rita Mae Brown

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **누적 Output** | CodeReview_20260419_1776642516.md |
| **Period** | 2026/04/19 22:58:18 - 2026/04/20 08:44:01 |
| **Model(Effort)** | claude-opus-4-7 (--effort max) |
| **Tools** | '/check' |

| 등급 | 건수 | 설명 |
| :--- | :--- | :--- |
| **P0:Critical** | 1개 | nullptr 역참조 제외 |
| **합계** | 1개 |   |

## P0:Critical - 2026/04/19

#### [P0:Nullptr Crash][정훈희][9991234][Test.cpp/TEST()/Line:1-7]
[원인] nullptr 역참조 크래시
```cpp
int* pT = nullptr;
생략...

printf("T5 %d.\n ", *pT);
```
 <details>
  <summary>상태 : [미결] , 위험 : 99, 횟수 : 5, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `pT`가 `nullptr`로 초기화된 후 line 12에서 `*pT`로 역참조하여 런타임 크래시 발생. `int TEST()` 함수 진입 시 dead code 블록을 지나 즉시 크래시.
  <br><br>- 의견 : 함수 자체가 테스트 목적이면 함수 제거 고려.
  <br><br>- 기타 : 커밋 `b41368f`에서 T7 `*pT` 역참조가 추가로 재도입되어 동일 변수에 대한 중복 위험.
 </details>
 - 사유 : 일단 제외
