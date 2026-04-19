
@echo off

set "CLD=D:/SRC/ServerReview"
set "BIN=D:/SRC/ServerReview/bin"
set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

@echo "CodeReview_01"

claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort high "%BIN%/CodeReview_01.md Execute"
