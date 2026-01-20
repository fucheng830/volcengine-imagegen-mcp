@echo off
echo ========================================
echo   火山引擎 AI 生图 MCP 服务器
echo   快速启动脚本
echo ========================================
echo.

REM 检查是否设置了 API Key
if "%ARK_API_KEY%"=="" (
    echo [错误] 未设置 ARK_API_KEY 环境变量
    echo.
    echo 请先设置 API Key：
    echo   Windows CMD:   set ARK_API_KEY=你的API密钥
    echo   PowerShell:     $env:ARK_API_KEY="你的API密钥"
    echo.
    pause
    exit /b 1
)

echo [信息] ARK_API_KEY 已设置
echo [信息] 正在启动 MCP 服务器...
echo.
echo 提示：服务器启动后，请在 MCP Client (如 Claude Desktop) 中添加以下配置：
echo   名称: volcengine-imagegen-mcp
echo   命令: npx volcengine-imagegen-mcp
echo   环境变量: ARK_API_KEY=%ARK_API_KEY%
echo.

REM 检查是否已构建
if not exist "dist\index.js" (
    echo [信息] 未检测到构建文件，正在执行构建...
    call npm run build
    if errorlevel 1 (
        echo [错误] 构建失败
        pause
        exit /b 1
    )
)

echo [信息] 启动 MCP 服务器...
npm start

pause
