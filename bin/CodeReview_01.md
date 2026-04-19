# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## REVIEW

**RV1: .cpp,.h,.lua,.json,.xml,.ini만 검사**
 
**RV2: HEAD 소스 기준으로 이슈 확인**

**RV3: 전체적인 소스 변경점을 먼저 파악 후 이슈별 연관된 최근 커밋들 확인**

**RV4: 발견된 이슈의 커밋과 관련된 최신 소스를 체크하여 유사한 문제나 사이드 이펙트가 없는지 확인**

**RV5: 커밋별로 이슈 정리할 때, 전체적으로 이슈 누락이나 중복 또는 해결이 없는지 확인**

**RV6: 로그인/아웃(중복 접속, 로딩 처리, 좀비, 고스트 등), 재화(Money, Ruby, Bonus, Item 등), 손실/제재/결제(Restriction, Regulation, Consume), 게임플레이(Play, Room, Result) 관련 부분은 연관된 상위 호출 부분까지 자세하고 세밀하게 검토**

**RV7: 스키마 형상 관리나 클라 패킷 하위 호환성, Test Code, Cheat Command, Tracking Log, Tool 관련 된 부분은 중요도를 조금 낮게 책정**

## EXCUTE

- Excute1: './bin/CodeReview.md' Loading

- Excute2: {$SrcPoint}에 {$GitSync}

- Excute3: {$Python} clean-output

- Excute4: {$Command} "{$SrcPoint}에서만(다른 파일 참조 금지) {$Scope} 코드 리뷰" → 리뷰 결과만 이슈별로 [미결]과 [해결]로 분류하여 최신{$Output}를 생성하여 병합

- Excute5: 최신{$Output}의 맨위에 요약 저장
