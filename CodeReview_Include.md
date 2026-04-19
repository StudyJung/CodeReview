## P0:Critical - 2026/04/19

#### [P0:Crash nullptr][정훈희][f625d50][Test.cpp/TEST()/Line:12]
nullptr 포인터 pT 역참조 크래시
```
int* pT = nullptr;
...
printf("T5 %d.\n ", *pT);
```
pT nullptr 역참조 제거 필요
```
int* pT = nullptr;
...
if (pT != nullptr)
{
    printf("T5 %d.\n ", *pT);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `TEST()` 함수 내 `int* pT = nullptr;`로 초기화된 포인터를 `printf("T5 %d.\n ", *pT);`에서 역참조하여 런타임 nullptr 크래시 발생. 커밋 `f625d50`에서 신규 추가된 라인임.
  <br><br>- 의견 : 해당 `printf` 라인 제거 또는 `pT != nullptr` null 체크 후 역참조. 커밋 메시지는 "TEST pT printf removed"라고 서술되어 있으나 실제 diff는 반대로 라인을 추가하고 있어 커밋 의도와 코드가 불일치 → 즉시 제거 권장.
  <br><br>- 기타 : 동일 파일 내 `*p5`(Line:9, `if(false)` 사각지대지만 심볼 정의 없음), `*pP`(Line:25, 정의 없는 심볼) 등 유사 패턴 다수 존재. Test 코드(RV7: 중요도 하향 대상)지만 nullptr 역참조는 결정적 크래시이므로 P0 유지.
 </details>

#### [P0:Crash nullptr][정훈희][f625d50][Test.cpp/main()/Line:21]
nullptr 포인터 pM 역참조 크래시
```
int* pM = nullptr;

printf("T1 %d.\n ", *pM);
```
pM nullptr 역참조 제거 필요
```
int* pM = nullptr;

if (pM != nullptr)
{
    printf("T1 %d.\n ", *pM);
}
```
 <details>
  <summary>상태 : [미결] , 위험 : 95, 횟수 : 1, 추적 : 2026/04/19 - 2026/04/19</summary>
  <br>- 설명 : `main()` 함수 내 `int* pM = nullptr;`로 초기화된 포인터를 `printf("T1 %d.\n ", *pM);`에서 역참조하여 프로세스 엔트리 실행 즉시 nullptr 크래시 발생. 커밋 `f625d50`에서 신규 추가된 라인임.
  <br><br>- 의견 : 해당 `printf` 라인 제거 또는 `pM != nullptr` null 체크 후 역참조. `main()` 최초 진입 직후에서 발생하므로 전체 프로세스 기동 불가 상태.
  <br><br>- 기타 : 동일 파일·동일 커밋에서 `*pT` nullptr 역참조와 쌍으로 추가됨. Test 코드(RV7)지만 main 진입 직후 확정 크래시이므로 P0 유지. `*pP`(Line:25) 미정의 심볼은 기존 이슈로 범위 외.
 </details>
