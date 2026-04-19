
@echo off

set "CLD=D:/SRC/CodeReview"
set "BIN=D:/SRC/CodeReview/bin"
set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

@echo "CodeReview_02"

claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort high "%BIN%/CodeReview_02.md Execute"
