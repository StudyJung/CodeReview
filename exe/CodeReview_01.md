# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## REVIEW

**RV1: .cpp,.h,.lua,.json,.xml,.ini만 검사**
 
**RV2: 최신 소스 기준으로 전체적인 소스 변경점을 먼저 파악 후 이슈별 연관된 최근 커밋들 확인**

**RV3: 발견된 이슈의 커밋과 관련된 최신 소스를 체크하여 유사한 문제나 사이드 이펙트가 없는지 확인**

**RV4: 커밋별로 이슈 정리할 때, 전체적으로 이슈 누락이나 중복 또는 해결이 없는지 확인**

**RV5: 로그인/아웃(중복 접속, 로딩 처리, 좀비, 고스트 등), 재화(Money, Ruby, Bonus, Item 등), 손실/제재/결제(Restriction, Regulation, Consume), 게임플레이(Play, Room, Result) 관련 부분은 연관된 상위 호출 부분까지 자세하고 세밀하게 검토**

**RV6: 원인 코드 소스 주석이 이슈와 동일하다면 중요도를 조금 낮게 책정**

**RV7: 스키마 형상 관리나 클라 패킷 하위 호환성, Test Code, Cheat Command, Tracking Log, Tool 관련 된 부분은 중요도를 조금 낮게 책정**

## MUST

**{$Include}, {$Exclude}, {$Resolve}, {$Minority}, {$Workers} 파일들 절대 사용 금지**

## EXECUTE

- Execute01_1: './exe/CodeReview.md', './exe/CodeReview.py' Loading

- Execute01_2: {$SrcPoint}에 {$GitSync}

- Execute01_3: {$Python} clean-output

- Execute01_4: {$Command} "{$SrcPoint}에서만 {$Scope}범위 코드 리뷰" → 코드 리뷰 결과들을 [미결]과 [해결]로 분류

- Execute01_5: 코드 리뷰 결과 [미결] 이슈들만 최신{$Output}을 생성하여 저장

- Execute01_6: 최신{$Output}의 맨위에 요약 갱신 저장

- Execute01_7: {$WrkPoint}에 {$GitSync}
