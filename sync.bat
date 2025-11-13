@echo off
chcp 65001 >nul
echo 开始同步 LeetCode 题目...
echo.

echo 步骤 1: 更新题目分类...
leetcode-tool update
if errorlevel 1 (
    echo 更新分类失败！
    pause
    exit /b 1
)

echo.
echo 步骤 2: 同步到 Notion...
:retry_notion
leetcode-tool sync --notion
if errorlevel 1 (
    echo.
    echo 同步失败，可能是网络问题。是否重试？(Y/N)
    set /p retry="请输入: "
    if /i "%retry%"=="Y" (
        echo 正在重试...
        timeout /t 3 /nobreak >nul
        goto retry_notion
    ) else (
        echo 跳过 Notion 同步，继续提交到 GitHub...
    )
)

echo.
echo 步骤 3: 提交到 GitHub...
git add .
set /p commitMessage="请输入提交信息（直接回车使用默认信息）: "
if "%commitMessage%"=="" set commitMessage=feat: 完成题目并同步到 Notion
git commit -m "%commitMessage%"
git push origin main

echo.
echo 同步完成！
pause

