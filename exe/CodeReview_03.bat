
@echo off

set "CLD=D:/SRC/Base"
set "BIN=D:/SRC/CodeReview/exe"
::set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

@echo "CodeReview_03"

claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort high "%BIN%/CodeReview_03.md Execute"

if errorlevel 1 (
    echo Claude failed, fallback to Codex
    codex exec --yolo -m gpt-5.4 "Execute" < "%BIN%\CodeReview_03.md" >nul 2>&1
)
