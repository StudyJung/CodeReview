
@echo off

set "CLD=D:/SRC/CodeReview"
set "BIN=D:/SRC/CodeReview/exe"
::set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

@echo "CodeReview_02"

claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort max "%BIN%/CodeReview_02.md Execute"
::type "%BIN%/CodeReview_02.md" | codex exec --yolo -m gpt-5.4 "Execute"
