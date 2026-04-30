
@echo off

set "CLD=D:/SRC/Base"
set "BIN=D:/SRC/CodeReview/exe"
::set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

@echo "CodeReview_02"

claude --dangerously-skip-permissions --model claude-opus-4-7 --effort max "%BIN%/CodeReview_02.md Execute"

if errorlevel 1 (
    echo Claude failed, fallback to Codex
    codex exec --yolo -m gpt-5.5 -c model_reasoning_effort=xhigh "Execute" < "%BIN%\CodeReview_02.md"
)
