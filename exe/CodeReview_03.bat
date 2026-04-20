
@echo off

set "CLD=D:/SRC/Base"
set "BIN=D:/SRC/CodeReview/exe"
::set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

@echo "CodeReview_03"

claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort max "%BIN%/CodeReview_03.md Execute"
::type "%BIN%/CodeReview_03.md" | codex exec --yolo -m gpt-5.4 "Execute"
