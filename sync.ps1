# 同步脚本：更新分类并同步到 Notion 和 GitHub

Write-Host "开始同步 LeetCode 题目..." -ForegroundColor Green

# 1. 更新分类
Write-Host "`n步骤 1: 更新题目分类..." -ForegroundColor Yellow
leetcode-tool update
if ($LASTEXITCODE -ne 0) {
    Write-Host "更新分类失败！" -ForegroundColor Red
    exit 1
}

# 2. 同步到 Notion
Write-Host "`n步骤 2: 同步到 Notion..." -ForegroundColor Yellow
leetcode-tool sync --notion
if ($LASTEXITCODE -ne 0) {
    Write-Host "同步到 Notion 失败！" -ForegroundColor Red
    exit 1
}

# 3. 提交到 GitHub
Write-Host "`n步骤 3: 提交到 GitHub..." -ForegroundColor Yellow
git add .
$commitMessage = Read-Host "请输入提交信息（直接回车使用默认信息）"
if ([string]::IsNullOrWhiteSpace($commitMessage)) {
    $commitMessage = "feat: 完成题目并同步到 Notion"
}
git commit -m $commitMessage
git push origin main

Write-Host "`n同步完成！" -ForegroundColor Green

