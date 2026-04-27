# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## REVIEW

**RV1: 코드 리뷰는 .cpp,.h,.lua,.json,.xml,.ini만 검사**

**RV2: Crash, Memory leak, Dangling Pointer 관련은 중요도를 많이 높게 책정(위험도 많이 추가)**

**RV3: 로그인/아웃(중복 접속, 로딩 처리, 좀비, 고스트 등), 재화(Money, Ruby, Bonus, Item 등), 손실/제재/결제(Restriction, Regulation, Consume), 게임플레이(Play, Room, Result), 클라이언트 패킷 값 체크 관련은 연관된 상하위 호출 부분까지 자세하고 세밀하게 검토 후 중요도를 조금 높게 책정(위험도 조금 추가)**

**RV4: SQL Injection, Silent Bypass(if,switch,for), Dup Skip Return, Timezone Localtime 관련은 중요도를 조금 낮게 책정(위험도 조금 감소)**

**RV5: 원인 코드 소스 주석이 이슈와 비슷하거나 스키마 형상 관리, 하위 호환성, Test, Cheat, Track, Tool 관련은 중요도를 많이 낮게 책정(위험도 많이 감소)**

## MUST

**{$Include}, {$Exclude}, {$Resolve}, {$Minority}, {$Workers}, CodeReviewAI.md 절대 사용 금지**

## EXECUTE

* Execute01_1: '{$WrkPoint}/exe/{$Main}', '{$WrkPoint}/exe/{$Python}' Loading
* Execute01_2: {$SrcPoint}에 {$GitSync}
* Execute01_3: {$Python} clean-output
* Execute01_4: {$Command} "{$SrcPoint}에서만 {$Scope}범위로만 코드 리뷰"
* Execute01_5: 코드 리뷰 결과들을 HEAD 소스 기준으로 이슈와 이슈의 상하위 함수들 및 이슈가 호출되는 소스들을 체크하여 [해결]과 [미결]로 분류
* Execute01_6: 코드 리뷰 결과들 중 [미결] 이슈들만 RV1-5 규칙을 적용하여 중요도와 위험도 및 가장 관련 깊은 커밋(해쉬/담당자) 책정
* Execute01_7: 코드 리뷰 결과들 중 [미결] 이슈들만 원인 코드와 이슈 커밋(해쉬/담당자)의 소스 변경점이 일치하는지 다시 확인 → 일치하지 않을 경우 리뷰 내 커밋들을 다시 확인 → 리뷰 내 커밋들에 없다면 '000000/미지정'로 지정
* Execute01_8: 최신{$Output}을 생성하여 코드 리뷰 결과 중 [미결] 이슈들만 저장하고, 맨위에 요약 정보 추가
* Execute01_9: {$WrkPoint}에 {$GitSync}
