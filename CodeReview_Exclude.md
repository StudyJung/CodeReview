#### [P0:Nullptr Crash][정훈희][9991234][Test.cpp/TEST()/Line:1-7]
[원인] nullptr 역참조 크래시
```cpp
int* pT = nullptr;

...

printf("T5 %d.\n ", *pT);
```
- 사유 : 일단 제외