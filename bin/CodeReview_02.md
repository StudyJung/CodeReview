# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## MUST

**{$Include} 파일만 쓰기 허용(나머지 파일들 쓰기 금지)**

## EXCUTE

- Excute1: './bin/CodeReview.md' Loading

- Excute2: {$Include}에 최신{$Output}의 P0-P1 이슈들만 병합 

- Excute3: {$Include}에 {$Exclude}의 모든 이슈들 삭제

- Excute4: {$WrkPoint}에 {$GitSync}
