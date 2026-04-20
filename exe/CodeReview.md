# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## VALUE

$WrkDir = D:/SRC/CodeReview

$WrkGit = https://github.com/StudyJung/CodeReview

$WrkPoint = $WrkDir

$SrcDir = D:/SRC/CodeReview

$SrcGit = https://github.com/StudyJung/CodeReview

$SrcPoint = $SrcDir

$Branch = main

$GitSync = Git(Add -> Commit -> Pull -> Push -> Merge)

$Python = CodeReview.py

$Include = CodeReview_Include.md

$Exclude = CodeReview_Exclude.md

$Minority = CodeReview_Minority.md

$Resolve = CodeReview_Resolve.md

$Workers = CodeReview_'작업자'.md(예:CodeReview_정훈희.md - 작업자 = 정훈희)

$Branch = main

$GitSync = Git(Add -> Commit -> Pull -> Push -> Merge)

$Python = CodeReview.py

$Include = CodeReview_Include.md

$Exclude = CodeReview_Exclude.md

$Minority = CodeReview_Minority.md

$Resolve = CodeReview_Resolve.md

$Output = CodeReview_년월일_UnixTime.md(예: CodeReview_20020301_1617181920.md)

$Python = CodeReview.py

$Command = 오늘이 (일,월,수,목)요일이면 '/check'만 사용, 나머지이면 '/review'만 사용

$Scope = 오늘이 (일,수,토)요일이면 'LastTag이후 ~ HEAD까지 코드 리뷰', 나머지는 '2주일전 ~ HEAD까지 코드 리뷰'

## FUNCTION

* 위험도 = 01~99점까지 위험이 클수록 높은 점수 <- 중요도 상승, 하락 등에 수치 조정({$Include}에서 P0, P1 이슈만)

* 중요도 = P0:Critical, P1:High, P2:Medium, P3:Low, P4:Minimal(위험도 10점미만 P4보정) <- 이슈 우선 순위 판단하여 업데이트

* 이슈매칭 = 키(제목·커밋·해쉬·라인 등) 완전 일치가 아닌, 제목·파일·함수·설명·내용 등 기준 의미적 동일성으로 판단. 특히 핵심 원인 코드 1줄 변화 비교 주의해서 확인.

* 이슈카운트 = 최신{$Output}의 경우 1, {$Include}에 병합 시점에 신규 이슈라면 1 기존 이슈라면 +1

## FUNCTION

* 위험도 = 01~99점까지 위험이 클수록 높은 점수 <- 중요도 상승, 하락 등에 수치 조정({$Include}에서 P0, P1 이슈만)

* 중요도 = P0:Critical, P1:High, P2:Medium, P3:Low, P4:Minimal(위험도 10점미만 P4보정) <- 이슈 우선 순위 판단하여 업데이트

* 이슈매칭 = 키(제목·커밋·해쉬·라인 등) 완전 일치가 아닌, 제목·파일·함수·설명·내용 등 기준 의미적 동일성으로 판단. 특히 핵심 원인 코드 1줄 변화 비교 주의해서 확인.

* 이슈카운트 = 최신{$Output}의 경우 1, {$Include}에 병합 시점에 신규 이슈라면 1 기존 이슈라면 +1

## FILE

**모든 파일들은 미리 읽지말고, 꼭 필요한 곳에서만 읽음**

**UTF-8 NO BOM**

**TitemZone=TZ=Korea, UTC KST**

**반드시 {$WrkPoint}안의 ({$Include}, {$Exclude}, {$Resolve}, {$Minority}, {$Workers}, {$Output}) 파일들만 사용**

**{$Include}, {$Exclude}, {$Resolve}, {$Minority} 파일들이 없다면 생성**

**{$Resolve}, {$Minority}, {$Workers} 파일들은 절대 읽기 금지, 오직 쓰기만 사용**

**'./obj'폴더와 {$Resolve}, {$Minority}, {$Workers}는 추론에 절대 사용 금지(축약 및 이슈 수정 금지)**

## RULE

**EXECUTE의 내용만 행동(EXECUTE 외 다른 행동 절대 금지)**

**EXECUTE의 실행 순서를 철저히 지킴(EXECUTE 실행 순서 변경 절대 금지)**

## REPORT - 리포트 이슈와 요약 작성

**이슈 내용 보장, 이슈 축약 금지**

**병합은 최신 내용으로 작성하되 기존 내용을 보완해서 저장**

**요약 및 이슈는 제목 포함 정해진 형식만으로 구성하며 '사유' 제외 모든 항목 기입 필수**

**[해결] 시점에만 기존 사유 내용에 병합(사유 변경 금지)**

**모든 파일에 정해진 형식의 이슈와 요약만 작성(이슈와 요약 외 작성 금지)**

**파일에 새로운 이슈를 추가하거나 기존 이슈를 병합할 경우 '중요도 > 위험도'별 맨위에 저장**

**이슈 [해결]은 코드 변경 또는 주석 처리가 없거나 관련 커밋이 없는 경우 해결 금지, 중요도와 위험도를 조정**

**지워진 파일이 필요한 경우 복구하지말고, 새로 생성**

### 요약(제목 포함)

``` 리포트 요약 예)
# {$Output} <- 제목은 리포트 파일명
- 농담이나 덕담 또는 명언 한마디 추가

## 요약
| 항목 | 내용 |
| :--- | :--- |
| **Git Range** | 2026/03_UPDATE - HEAD ( Commits 100 ) |
| **Period** | 2025/01/01 00:00:00 - 2025/03/03 11:33:33 <- Git Range Time |
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

1. [중요도:2개의 영단어 요약][작업자명 한글 이름 세글자만][대표 커밋 해쉬 1개][파일명 1개/함수면 또는 클래스명 1개/Line:33-100]
2. [원인] 짧게 내용 요약(7단어 이하 요약)
3. 원인 코드(1라인 이상 필수, 불필요 라인은 '생략...' 으로 생략하고 핵심 코드 위주)
4. [추천 또는 해결] 수정 내용 요약(7단어 이하 요약, P0일 경우에만 추가 )
5. 추천 또는 해결 코드([미결]일 경우 P0일 경우에만 추천 코드 추가, [해결]일 경우 해결 코드 추가)
6. <details></details>

```` 리포트 이슈 예)
## P0:Critical - 갱신일

#### [P0:Crash nullptr][홍길동][60dc356][Huns.cpp/main()/Line:16-17]
[원인] printf nullptr 역참조 크래시
``` 1줄 이상 필수
int* pM = nullptr;
생략...

printf("T1 %d.\n ", *pM);
```
[추천] 포인터 역참조 전 nullptr 체크 추가
``` 1줄 이상 필수
int* pM = nullptr;
생략...

if (pM != nullptr)
{
	printf("T1 %d.\n ", *pM);
}
```
 <details>
  <summary>상태 : [미결,해결] , 위험 : 99(위험도), 횟수 : 1(이슈카운트), 추적 : 2025/01/01 - 2025/03/03(이슈 생성일 - 갱신일)</summary>
  <br>- 설명 : `pT`이 `nullptr`로 초기화 후 `*pT`으로 역참조 런타임 크래시 발생 <- 문제 설명 상세하게 필수
  <br><br>- 의견 : `*pT` 대신 인트형으로 <- 수정 및 개선 등 상세하게 필수
  <br><br>- 기타 : `*pT`가 Add에서도 사용 중 또는 없음 <- 사이드 이펙트 체크, 유사 코드 존재 여부, 관련 문서 링크 등 추가 정보 등 코멘트
 </details>
 - 사유 : 없으면 제외. 해결 시점에만 해결한 내용 포함 또는 '[Exclude]' 또는 '[Include]' 주석이 있는 경우에 병합하지말고 계속 추가 <- 담당자 수동 기입도 가능

## P4:Minimal - 2025/03/01

#### [P4:Low quality][아무개][cafa6ab][Jung.h/global/Line:33]
[원인] iostream 미사용
```
#include <iostream>
```
 <details>
  <summary>상태 : [미결] , 위험 : 03, 횟수 : 3, 추적 : 2025/03/01 - 2025/04/03</summary>
  <br>- 설명 : iostream 미사용
  <br><br>- 의견 : 없애라
 </details>

#### [P4:Quality low][아무개][cafa6ab][Huns.h/global/Line:1]
[원인] iostream 포함했으나 미사용
```
#include <iostream>
```
[해결] iostream 삭제
```

```
 <details>
  <summary>상태 : [해결] , 위험 : 07, 횟수 : 1, 추적 : 2025/01/01 - 2025/03/03</summary>
  <br>- 설명 : iostream 포함했으나 미사용
  <br><br>- 의견 : 제거해라
 </details>
 - 사유 : iostream 삭제
````
