@echo off
title Chay Website Local - Nha Khoa Kim Dung
echo ========================================================
echo   DANG KHOI CHAY SERVER LOCAL CHO WEBSITE
echo ========================================================
echo.
echo   Trang chu se mo tai: http://localhost:8000
echo   De dung server: Nhan to hop phim Ctrl + C
echo.
echo ========================================================
cd /d "%~dp0\website"
start http://localhost:8000
python -m http.server 8000
pause

