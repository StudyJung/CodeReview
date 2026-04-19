# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## VALUE

$WrkDir = D:/SRC/CodeReview

$WrkGit = https://github.com/StudyJung/CodeReview

$WrkPoint = $WrkDir

$SrcDir = D:/SRC/CodeReview

$SrcGit = https://github.com/StudyJung/CodeReview

$SrcPoint = $SrcDir

$Include = CodeReview_Include.md

$Exclude = CodeReview_Exclude.md

$Resolve = CodeReview_Resolve.md

$Worker = CodeReview_'작업자'.md

$Output = CodeReview_년월일_UnixTime.md

$Command = '/check'

$Scope = 'LastTag이후 ~ HEAD까지 코드 리뷰'

## REPORT - 리포트 이슈와 요약 작성

### 요약(제목 포함)

``` 리포트 요약 예)
# {$Output} <- 제목은 리포트 파일명
- 농담이나 덕담 또는 명언 한마디 추가

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **Git Range** | 2026/03_UPDATE - HEAD ( Commits 100 ) |
| **Period** | 2025/01/01 00:00:00 - 2025/03/03 11:33:33 |
| **Model(Effort)** | claude-opus-4-6 (--effort max) <- 사용 AI model |
| **Tools** | '/fd -t check', '/check', '/review', '/teammates_check' <- 사용 {$Command} |

| 등급 | 건수 | 설명 |
| :--- | :--- | :--- |
| **P0:Critical** | 10개 | 널 역참조, 데이터 유실, 레이스 컨디션  |
| **P1:High** | 20개 | 보안, 로직 오류, 리소스 누수  |
| P2:Medium | 30개 | 성능, 검증 누락  |
| P3:Low | 40개 | 컨벤션, 가독성  |
| **합계** | 100개 |   |
```
 
### 이슈(내용 포함)

[중요도:2개의 영단어 요약][작업자 이름만][대표 커밋 해쉬 한개만][파일 이름만/함수 또는 클래스 이름만/Line]
짧게 내용 요약

```` 리포트 이슈 예)
## P0:Critical - 갱신일

#### [P0:Crash nullptr][홍길동][60dc356][Huns.cpp/main()/Line:16-17]
printf nullptr 역참조 크래시
``` 1줄 이상 필수
printf("Hello1 T %x. ", *pT);
printf("Hello2 T %n. ", pT);
```
 <details>
  <summary>상태 : [미결,해결] , 위험 : 99(위험도), 추적 : 2025/01/01 - 2025/03/03(이슈 생성일 - 갱신일)</summary>
  <br>- 설명 : `pT`이 `nullptr`로 초기화 후 `*pT`으로 역참조 런타임 크래시 발생 <- 문제 설명 상세하게 필수
  <br><br>- 의견 : `*pT` 대신 인트형으로 <- 수정 및 개선 등 상세하게 필수
  <br><br>- 기타 : `*pT`가 Add에서도 사용 중 또는 없음 <- 사이드 이펙트 체크, 유사 코드 존재 여부, 관련 문서 링크 등 추가 정보 등 코멘트
 </details>

## P4:Minimal - 2025/03/01

#### [P4:Quality low][아무개][cafa6ab][Huns.h/global/Line:1]
iostream 포함했으나 미사용
```
#include <iostream>
```
 <details>
  <summary>상태 : [미결] , 위험 : 07, 추적 : 2025/01/01 - 2025/03/03</summary>
  <br>- 설명 : iostream 포함했으나 미사용
  <br><br>- 의견 : 제거해라
 </details>
````

## EXCUTE

- Excute1: 코드 리뷰 중 ({$SrcPoint}에 '[Include]' 주석있는 이슈는 {$Include}에 병합, {$SrcPoint}에 '[Exclude]' 주석있는 이슈는 {$Exclude}에 병합)

- Excute2: {$Command} "{$SrcPoint}에서 Excute2를 포함하여 {$Scope}범위 코드 리뷰"

- Excute3: 코드 리뷰 후 (맨위에 요약을 포함하여 [미결]이슈들만 최신{$Outp,ut}를 생성하여 병합)
- 
- Excute4: {$Include}에 최신{$Output}의 P0-P1 이슈들만 병합 후 {$Include}에 {$Exclude}의 모든 이슈들 삭제

- Excute5: {$Include}의 [미결]이슈들을 {$SrcPoint}에서만 해결 검사 후 해결된 이슈는 {$Include}에만 [해결]로 변경

- Excute6: {$Include}의 [해결]이슈들을 {$Resolve}에 저장, {$Include}의 P0-P1 이슈들은 작업자별 파일 재생성 후 저장
