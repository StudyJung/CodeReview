# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## MUST

**{$Resolve}, {$Minority}, {$Worker} 파일들 절대 사용 금지**

## EXECUTE

- Execute02_1: './bin/CodeReview.md' Loading

- Execute02_2: {$Include}에 최신{$Output}의 P0-P1 이슈들만 병합(중요도,횟수,점수,갱신일 업데이트) 

- Execute02_3: {$Include}에 {$Exclude}의 모든 이슈들 삭제

- Execute02_4: {$Include}의 [미결] 이슈들마다 {$SrcPoint}에서 해결되었다면 {$Include}에만 [해결]로 변경

- Execute02_5: {$Include}의 맨위에 요약 갱신 저장

- Execute02_6: {$WrkPoint}에 {$GitSync}
