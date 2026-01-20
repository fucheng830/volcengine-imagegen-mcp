# ========================================
#   火山引擎 AI 生图 MCP 服务器
#   快速启动脚本 (PowerShell)
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  火山引擎 AI 生图 MCP 服务器" -ForegroundColor Cyan
Write-Host "  快速启动脚本 (PowerShell)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查是否设置了 API Key
$apiKey = $env:ARK_API_KEY
if (-not $apiKey) {
    Write-Host "[错误] 未设置 ARK_API_KEY 环境变量" -ForegroundColor Red
    Write-Host ""
    Write-Host "请先设置 API Key：" -ForegroundColor Yellow
    Write-Host "  PowerShell:     `$env:ARK_API_KEY='你的API密钥'`" -ForegroundColor White
    Write-Host ""
    Write-Host "设置后重新运行此脚本" -ForegroundColor Yellow
    Read-Host "按任意键退出..."
    exit 1
}

Write-Host "[信息] ARK_API_KEY 已设置" -ForegroundColor Green
Write-Host "[信息] 正在启动 MCP 服务器..." -ForegroundColor Green
Write-Host ""
Write-Host "提示：服务器启动后，请在 MCP Client (如 Claude Desktop) 中添加以下配置：" -ForegroundColor Cyan
Write-Host "  名称: volcengine-imagegen-mcp" -ForegroundColor White
Write-Host "  命令: npx volcengine-imagegen-mcp" -ForegroundColor White
Write-Host "  环境变量: ARK_API_KEY=$($env:ARK_API_KEY)" -ForegroundColor White
Write-Host ""

# 检查是否已构建
if (-not (Test-Path "dist\index.js")) {
    Write-Host "[信息] 未检测到构建文件，正在执行构建..." -ForegroundColor Yellow
    npm run build
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[错误] 构建失败" -ForegroundColor Red
        Read-Host "按任意键退出..."
        exit 1
    }
}

Write-Host "[信息] 启动 MCP 服务器..." -ForegroundColor Green
npm start
