#### [P0:Nullptr Crash][정훈희][321f4c5][Test.cpp/main()/Line:11]
`main()` 역참조 크래쉬
``` 문제 코드
int* pM = nullptr;
printf("T1 %d.\n ", *pM);
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `printf` 가변 인자로 `*pM`을 전달. 함수 호출 스택 구성 시점에 역참조가 일어나 엔트리 포인트 진입 직후 크래시
  <br><br>- 의견 :  nullptr 체크 추가
  <br><br>- 기타 : `TEST()` Line:7 이슈와 묶어 동시 수정 권장.
 </details>