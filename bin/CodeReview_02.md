# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## MUST

**{$Resolve}, {$Minority}, {$Worker} 파일들 절대 사용 금지**

## EXCUTE

- Excute021: './bin/CodeReview.md' Loading

- Excute022: {$Include}에 최신{$Output}의 P0-P1 이슈들만 병합(중요도,횟수,점수,갱신일 업데이트) 

- Excute023: {$Include}에 {$Exclude}의 모든 이슈들 삭제

- Excute024: {$Include}의 [미결] 이슈들마다 {$SrcPoint}에서 해결되었다면 {$Include}에만 [해결]로 변경

- Excute025: {$WrkPoint}에 {$GitSync}
