# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## REVIEW

**RV1: .cpp,.h,.lua,.json,.xml,.ini만 검사**

**RV2: 최신 소스 기준으로 전체적인 소스 변경점을 먼저 파악 후 이슈별 연관된 리뷰 범위내 커밋들 확인**

**RV3: 발견된 이슈의 커밋과 관련된 최신 소스의 상하위 함수들를 체크하여 유사한 문제나 사이드 이펙트가 없는지 확인**

**RV4: 커밋별로 이슈 정리할 때, 전체적으로 이슈 누락이나 중복 또는 해결이 없는지 확인**

**RV5: 로그인/아웃(중복 접속, 로딩 처리, 좀비, 고스트 등), 재화(Money, Ruby, Bonus, Item 등), 손실/제재/결제(Restriction, Regulation, Consume), 게임플레이(Play, Room, Result), 크래쉬, 메모리, 포인터, 클라이언트 패킷 값 체크 관련은 연관된 상위 호출 부분까지 자세하고 세밀하게 검토 후 중요도를 조금 높게 책정(위험도 추가)**

**RV6: Memory leak 관련은 중요도를 조금 높게 책정(위험도 조금 추가)**

**RV7: SQL Injection, Silent Bypass(if,switch,for), Dup Skip Return, Timezone Localtime 관련은 중요도를 조금 낮게 책정(위험도 조금 감소)**

**RV8: 원인 코드 소스 주석이 이슈와 비슷하거나 스키마 형상 관리, 하위 호환성, Test, Cheat, Track, Tool 관련은 중요도를 많이 낮게 책정(위험도 많이 감소)**

**RV9: 원인 코드와 이슈의 커밋(해쉬, 담당자)의 변경점이 맞는지 다시 한번 확인하여 보정. 원인 코드를 이슈 커밋들의 변경점에서 찾을 수 없다면 커밋 해쉬와 담당자를 '000000/미지정'로 지정**

## MUST

**{$Include}, {$Exclude}, {$Resolve}, {$Minority}, {$Workers}, CodeReviewAI.md 절대 사용 금지**

## EXECUTE

* Execute01_1: '{$WrkPoint}/exe/{$Main}', '{$WrkPoint}/exe/{$Python}' Loading
* Execute01_2: {$SrcPoint}에 {$GitSync}
* Execute01_3: {$Python} clean-output
* Execute01_4: {$Command} "{$SrcPoint}에서만 {$Scope}범위로만 코드 리뷰" → RV1-9 규칙으로 코드 리뷰 결과 중 이슈들을 커밋별로 [미결]과 [해결]로 분류하여 중요도와 위험도 및 담당자 책정
* Execute01_5: 코드 리뷰 결과 [미결] 이슈들만 최신{$Output}을 생성하여 저장
* Execute01_6: 최신{$Output}의 맨위에 요약 갱신 저장
* Execute01_7: {$WrkPoint}에 {$GitSync}
