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
- 사유 : 일단 제외
