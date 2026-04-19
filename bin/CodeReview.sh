#!/usr/bin/env bash

# OX-PLow : https://blog.naver.com/study_jung/224251607299

set -u

CLD="${CLD:-$HOME/CodeReview}"
BIN="${BIN:-$CLD/bin}"
CODEX_CMD="${CODEX_CMD:-$(command -v codex || true)}"

cd "$CLD"

DAY=$((10#$(date +%d) % 10))
MOD=$((DAY % 2))
EFF=$((DAY % 6))

if [ "$MOD" -eq 1 ]; then
    MODEL="claude-opus-4-7"
else
    MODEL="sonnet-4-6"
fi

echo "$(date '+%Y-%m-%d'), ${DAY}, ${MOD}, ${EFF} --model ${MODEL}"

echo "CodeReview_01"
claude --dangerously-skip-permissions --model "${MODEL}" --effort max -p "${BIN}/CodeReview_01.md Execute"

echo "CodeReview_02"
claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort max -p "${BIN}/CodeReview_02.md Execute"

echo "CodeReview_03"
claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort max -p "${BIN}/CodeReview_03.md Execute"
# "${CODEX_CMD}" exec --yolo -m gpt-5.4 "Execute" < "${BIN}/CodeReview_03.md" >/dev/null 2>&1
