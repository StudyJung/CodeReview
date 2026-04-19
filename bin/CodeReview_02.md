# CodeReview [ABSOLUTE | STRICT ORDER | NO SKIP | SILENT | PRODUCTION]

## MUST

**최신{$Output}, {$Include} 파일만 쓰기 허용. 나머지 쓰기 금지**

## EXCUTE

- Excute1: './bin/CodeReview.md' Loading

- Excute2: {$Include}에 최신{$Output}의 P0-P1 이슈들만 병합 

- Excute3: {$Include}에 {$Exclude}의 모든 이슈들 삭제

- Excute4: {$Include}의 [미결]이슈들을 {$SrcPoint}에서 [해결] 검사 → 해결된 이슈는 {$Include}에만 [해결]로 변경
