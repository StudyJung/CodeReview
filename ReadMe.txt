
https://blog.naver.com/study_jung/224251607299

----------------------------------------------------------------------------------------------

ClaudeCode 세팅 (Codex 선택 세팅)

Git 및 GitHub CLI 세팅

----------------------------------------------------------------------------------------------

1. 폴더 생성 - C:\개인\CodeReview

2. C:\개인\CodeReview에 자신의 깃헙(https://github.com/개인/CodeReview) 클론

3. https://github.com/StudyJung/CodeReview 에서 받은 모든 파일을 C:\개인\CodeReview에 복사

4. 자신의 깃헙(https://github.com/개인/CodeReview)으로 푸시

----------------------------------------------------------------------------------------------

CodeReview.bat 수정

 - set "CLD=E:\SRC\Server" <- AI 작업 폴더 지정(예 ClaudeCode가 실행될 곳)

 - set "BIN=E:\SRC\ServerReview\bin" <- CodeReview 파일들 위치 지정

 - set "CODEX_CMD=%USERPROFILE%\AppData\Roaming\npm\codex.cmd" <- Codex를 사용할 경우에만 실행 파일 위치 지정

 - type "%BIN%\CodeReview_03.md" | codex exec --yolo -m gpt-5.4 "Execute" >nul 2>&1 <- Codex 사용

CodeReview.md 수정

 - 작업자 = 깃헙 작업자 이름들 추가
 
 - $WrkDir = C:\개인\CodeReview <- 자신의 코드 리뷰 결과 저장 폴더($WrkGit 클론)

 - $WrkGit = https://github.com/개인/CodeReview <- 자신의 코드 리뷰 결과 저장 깃헙

 - $WrkPoint = $WrkDir OR $WrkGit <- 결과 저장 위치 선택

 - $SrcDir = C:\개인\Source <- 자신의 소스 폴더($SrcGit 클론)

 - $SrcGit = https://github.com/개인/Source <- 자신의 소스 깃헙 

 - $SrcPoint = $SrcDir OR $SrcGit <- 소스 검색 위치 선택

 - $Command = 사용할 커맨드나 스킬 등 입력

----------------------------------------------------------------------------------------------

사용

1. CodeReview.bat 더블 클릭으로실행 또는 윈도우 스케줄러 등에 등록하고 주기적 실행

확인

1. $WrkDir와 $WrkGit에서 파일 확인

테스트

1. CodeReview_01~03.bat 으로 스탭별 실행
