
@echo off

set "CLD=D:/SRC/ServerReview"
set "BIN=D:/SRC/ServerReview/bin"
set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

@echo "CodeReview_03"

claude --dangerously-skip-permissions --model claude-haiku-4-5 --effort medium "%BIN%/CodeReview_03.md Execute"
::type "%BIN%/CodeReview_03.md" | codex exec --yolo -m gpt-5.4 "Execute"
