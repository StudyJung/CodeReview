
:: OX-PLow : https://blog.naver.com/study_jung/224251607299

@echo off

set "CLD=D:/SRC/Base"
set "BIN=D:/SRC/CodeReview/exe"
set "CODEX_CMD=%USERPROFILE%/AppData/Roaming/npm/codex.cmd"

cd /d %CLD%

set /A DAY=(%date:~-1%)
set /A MOD=DAY %% 2
set /A EFF=DAY %% 6

if %MOD% equ 1 (
    set MODEL=claude-opus-4-7
) else (
    set MODEL=claude-sonnet-4-6
)

@echo %date%, %DAY%, %MOD%, %EFF% --model %MODEL%

@echo "CodeReview"

claude --dangerously-skip-permissions --model %MODEL% --effort max -p "%BIN%/CodeReview_01.md Execute"

if errorlevel 1 (
    @echo "Codex"
    type "%BIN%/CodeReview_01.md" | codex exec --yolo -m gpt-5.4 "Execute" >nul 2>&1
	type "%BIN%/CodeReview_02.md" | codex exec --yolo -m gpt-5.4 "Execute" >nul 2>&1
	type "%BIN%/CodeReview_03.md" | codex exec --yolo -m gpt-5.4 "Execute" >nul 2>&1
) else (
	@echo "Claude"
	claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort max -p "%BIN%/CodeReview_02.md Execute"
	claude --dangerously-skip-permissions --model claude-sonnet-4-6 --effort high -p "%BIN%/CodeReview_03.md Execute"
)
