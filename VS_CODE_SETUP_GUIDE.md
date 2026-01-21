# 🔧 VS Code MCP Server 配置指南

## 📋 前置要求

### 1. 安装 VS Code

确保你已安装 Visual Studio Code：
- 下载地址：https://code.visualstudio.com/

### 2. 安装 Cline 扩展

Cline 是一个支持 MCP 协议的 VS Code 扩展。

**安装步骤**：
1. 打开 VS Code
2. 按 `Ctrl+Shift+X` 打开扩展面板
3. 搜索 `Cline`
4. 点击 **Install** 安装扩展

**扩展信息**：
- 扩展名称：Cline
- 支持：MCP 协议
- 功能：AI 编程助手，集成 MCP 工具

---

## 🔧 配置 MCP Server

### 方法 1: 通过 VS Code 设置配置（推荐）

#### 步骤 1：打开 VS Code 设置

**快捷方式**：
- Windows/Linux: `Ctrl + ,` (逗号)
- macOS: `Cmd + ,` (逗号)

#### 步骤 2：搜索 MCP 设置

在搜索框中输入：
```
cline mcp
```

#### 步骤 3：添加 MCP Server 配置

找到 **Cline: MCP Servers** 设置项，点击 **Edit in settings.json**

在 `settings.json` 中添加以下配置：

```json
{
  "cline.mcpServers": {
    "volcengine-imagegen": {
      "command": "python",
      "args": [
        "d:\\程序\\workspace\\opensource\\volcengine-imagegen-mcp\\server.py"
      ],
      "env": {
        "ARK_API_KEY": "14bb7c84-411b-4729-9d45-d0ddaba61c41"
      }
    }
  }
}
```

**配置说明**：
- `command`: Python 可执行文件路径
- `args`: server.py 的完整路径
- `env.ARK_API_KEY`: 你的火山引擎 API Key

#### 步骤 4：保存配置

保存 `settings.json` 文件（`Ctrl+S`）

#### 步骤 5：重启 VS Code

重启 VS Code 使配置生效：
- 关闭 VS Code
- 重新打开

---

### 方法 2: 通过 settings.json 文件直接配置

#### 步骤 1：打开 settings.json

**方法 1**：
1. 按 `Ctrl+Shift+P` 打开命令面板
2. 输入 `Preferences: Open User Settings (JSON)`
3. 按 Enter 打开

**方法 2**：
1. 点击左下角齿轮图标 ⚙️
2. 选择 **Settings**
3. 点击右上角 `{}` 图标打开 JSON 模式

#### 步骤 2：添加 MCP 配置

在 `settings.json` 文件中添加以下内容：

```json
{
  // ... 其他设置 ...
  
  "cline.mcpServers": {
    "volcengine-imagegen": {
      "command": "python",
      "args": [
        "d:\\程序\\workspace\\opensource\\volcengine-imagegen-mcp\\server.py"
      ],
      "env": {
        "ARK_API_KEY": "14bb7c84-411b-4729-9d45-d0ddaba61c41"
      }
    }
  }
}
```

**注意事项**：
- 如果文件中已有其他设置，确保在最外层大括号内
- JSON 格式必须正确，注意逗号
- 路径中的反斜杠需要转义或使用正斜杠

#### 步骤 3：保存并重启

- 保存文件（`Ctrl+S`）
- 重启 VS Code

---

## 🔍 验证配置

### 步骤 1：打开 Cline 扩展

1. 按 `Ctrl+Shift+P` 打开命令面板
2. 输入 `Cline: Open`
3. 按 Enter 打开 Cline 侧边栏

### 步骤 2：检查 MCP 连接

在 Cline 对话框中输入：
```
列出所有支持的模型和它们的功能
```

如果配置正确，Cline 会调用 MCP Server 并返回模型列表。

**预期输出**：
```
📋 火山引擎豆包生图 - 支持的模型列表

- **doubao-seedream-4-5-251128**
  豆包生图 4.5 (最新，支持多格式)

- **doubao-seedream-4-0-250828**
  豆包生图 4.0

- **doubao-seedream-3-0-t2i-250415**
  豆包生图 3.0 文生图

- **doubao-seedream-3-0-i2i**
  豆包生图 3.0 图生图

🎨 支持的尺寸：
- 2K
- 4K
- 1024x1024
- 2048x2048
```

---

## 🛠️ 故障排查

### 问题 1：找不到 MCP Server

**症状**：
- Cline 提示无法连接到 MCP Server
- 工具列表为空

**解决方案**：

1. **检查 Python 路径**：
```powershell
# 在 PowerShell 中运行
python --version
where python
```

确保 Python 已正确安装。

2. **检查 server.py 路径**：
```powershell
# 检查文件是否存在
Test-Path "d:\程序\workspace\opensource\volcengine-imagegen-mcp\server.py"
```

应该返回 `True`。

3. **查看 Cline 日志**：
- 在 VS Code 中打开输出面板（`Ctrl+Shift+U`）
- 选择 "Cline" 通道
- 查看错误信息

---

### 问题 2：API Key 错误

**症状**：
- Cline 提示未设置 API Key
- 生成图片失败

**解决方案**：

1. **检查 .env 文件**：
```powershell
# 查看 .env 文件内容
Get-Content "d:\程序\workspace\opensource\volcengine-imagegen-mcp\.env"
```

确保 `ARK_API_KEY` 已设置。

2. **检查 settings.json 中的 env 配置**：
- 确认 API Key 完整且正确
- 确保没有多余的引号或空格

3. **重新测试 API Key**：
```python
# 在 Python 中测试
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('ARK_API_KEY')
print(f"API Key: {key[:20]}...{key[-10:]}" if key else "API Key 未设置")
```

---

### 问题 3：Python 依赖缺失

**症状**：
- 启动 MCP Server 时提示模块不存在
- 例如：`No module named 'fastmcp'`

**解决方案**：

```powershell
# 安装所有依赖
cd "d:\程序\workspace\opensource\volcengine-imagegen-mcp"
pip install fastmcp httpx pydantic python-dotenv
```

---

## 📝 配置示例

### 完整的 settings.json 示例

```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "Consolas, 'Courier New', monospace",
  "cline.mcpServers": {
    "volcengine-imagegen": {
      "command": "python",
      "args": [
        "d:\\程序\\workspace\\opensource\\volcengine-imagegen-mcp\\server.py"
      ],
      "env": {
        "ARK_API_KEY": "14bb7c84-411b-4729-9d45-d0ddaba61c41"
      }
    }
  },
  "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

---

## 🚀 开始使用

### 示例 1：生成简单图片

在 Cline 对话框中输入：
```
生成一张美丽的山水风景画
```

### 示例 2：使用完整参数

```
生成一张专业摄影师拍摄的商业肖像，自然光，眼神自信，背景简洁，8K分辨率，文本权重 7.5，添加水印
```

### 示例 3：生成 Base64 格式

```
生成一张企业 Logo，以 Base64 格式返回
```

### 示例 4：批量生成

```
生成 3 张不同风格的城市夜景
```

---

## 📚 相关资源

### 项目文档

- 📖 **主文档**: `README.md`
- 📖 **使用示例**: `EXAMPLES.md`
- 📖 **快速开始**: `QUICKSTART.md`
- 📖 **测试报告**: `FINAL_TEST_REPORT_20260121.md`

### 外部资源

- 🔗 **VS Code 下载**: https://code.visualstudio.com/
- 🔗 **Cline 扩展**: https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev
- 🔗 **MCP 协议**: https://modelcontextprotocol.io/

---

## 💡 提示

### 1. 路径问题

Windows 路径建议使用正斜杠 `/` 或双反斜杠 `\\`：

```json
// ✅ 推荐
"args": [
  "d:/程序/workspace/opensource/volcengine-imagegen-mcp/server.py"
]

// ✅ 也可以
"args": [
  "d:\\程序\\workspace\\opensource\\volcengine-imagegen-mcp\\server.py"
]

// ❌ 不推荐
"args": [
  "d:\程序\workspace\opensource\volcengine-imagegen-mcp\server.py"
]
```

### 2. API Key 安全

⚠️ **重要提示**：
- 不要将包含真实 API Key 的 `settings.json` 提交到 Git
- 在 `.gitignore` 中添加 `settings.json`
- 或使用环境变量而非硬编码 API Key

### 3. 性能优化

如果你频繁使用，可以考虑：

- 使用 `venv` 虚拟环境
- 减少 API 调用频率
- 缓存生成的图片

---

## ✅ 配置检查清单

使用以下清单确保配置正确：

- [ ] 已安装 VS Code
- [ ] 已安装 Cline 扩展
- [ ] Python 已正确安装
- [ ] 所有依赖包已安装
- [ ] server.py 路径正确
- [ ] ARK_API_KEY 已设置
- [ ] settings.json 格式正确
- [ ] 已重启 VS Code
- [ ] MCP Server 连接成功
- [ ] 工具列表显示正常

---

**配置完成后，你就可以在 VS Code 中使用火山引擎 AI 生图功能了！** 🚀

祝你使用愉快！🎉
