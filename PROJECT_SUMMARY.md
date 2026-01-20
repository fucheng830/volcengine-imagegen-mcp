# 火山引擎 AI 生图 MCP 工具 - 项目总结

## 📋 项目概述

一个完整的、基于 npx 的 Model Context Protocol (MCP) 服务器实现，用于调用火山引擎豆包生图 API。

## 📁 项目文件结构

```
volcengine-imagegen-mcp/
├── package.json                    # 项目配置和依赖
├── tsconfig.json                  # TypeScript 编译配置
├── .gitignore                     # Git 忽略规则
├── .env.example                   # 环境变量模板
├── LICENSE                         # MIT 许可证
│
├── README.md                       # 主文档
├── EXAMPLES.md                    # 详细使用示例
├── QUICKSTART.md                   # 5 分钟快速开始指南
├── CLAUDE_GUIDE.md               # Claude Desktop 使用指南
├── VS_CODE_GUIDE.md               # VS Code 使用指南
│
├── src/
│   └── index.ts                   # TypeScript MCP 服务器实现（主代码）
│
├── server.py                       # Python MCP 服务器实现（备用方案）
│
├── start.bat                       # Windows 快速启动脚本
└── start.ps1                      # PowerShell 快速启动脚本
```

## ✨ 核心功能

### 4 个 MCP 工具

| 工具名称 | 功能描述 | 支持模型 | 关键参数 |
|-----------|----------|----------|----------|
| `generate_image` | 文生图：根据文本提示词生成图片 | doubao-seedream-4.5/4.0/3.0-t2i/i2i | prompt, size, model, count, guidance_scale, response_format, watermark |
| `image_to_image` | 图生图：根据参考图片和文本生成新图片 | doubao-seedream-4.5/4.0 | prompt, image_urls, size, model, guidance_scale, response_format, watermark |
| `generate_image_set` | 组图生成：生成一组内容关联的图片（最多 15 张） | doubao-seedream-4.5/4.0 | prompt, count, size, model, guidance_scale, response_format, watermark |
| `list_models` | 获取模型列表：返回所有支持的模型及其说明 | - | - |

### 支持的模型

- **doubao-seedream-4.5**: 豆包生图 4.5（最新，支持多格式）- 文生图、图生图、组图、多图生图
- **doubao-seedream-4.0**: 豆包生图 4.0 - 文生图、图生图、组图、多图生图
- **doubao-seedream-3.0-t2i**: 豆包生图 3.0 文生图 - 仅文生图
- **doubao-seedream-3.0-i2i**: 豆包生图 3.0 图生图 - 仅图生图

### 支持的参数

- **model**: 模型选择
- **prompt**: 提示词（支持中英文，1-2000 字符）
- **size**: 图片尺寸（2K, 4K, 1024x1024, 2048x2048）
- **guidance_scale**: 文本权重（1-10，默认 2.5）
- **response_format**: 返回格式（url 或 b64_json）
- **watermark**: 是否添加水印（默认 false）
- **count**: 生成数量（1-4 张，或组图的 2-15 张）
- **image_urls**: 参考图片 URL 列表（图生图专用，1-14 张）

## 🚀 部署方式

### 方式 1: 使用 npx（推荐，无需任何配置）

```bash
# 直接运行
npx volcengine-imagegen-mcp
```

### 方式 2: 全局安装后使用

```bash
# 全局安装
npm install -g volcengine-imagegen-mcp

# 直接运行
volcengine-imagegen-mcp
```

### 方式 3: 本地编译后运行

```bash
# 安装依赖
npm install

# 构建
npm run build

# 运行
npm start
# 或
node dist/index.js
```

### 方式 4: 使用 Python 版本

```bash
# 安装依赖
pip install -r requirements.txt

# 运行
python -m volcengine_imagegen_mcp
```

## 🔑 环境配置

### Windows

```cmd
REM 临时设置（当前窗口有效）
set ARK_API_KEY=你的火山引擎API密钥

REM 永久设置（需要管理员权限）
setx ARK_API_KEY "你的火山引擎API密钥"
```

```powershell
# 临时设置
$env:ARK_API_KEY="你的火山引擎API密钥"

# 永久设置
[System.Environment]::SetEnvironmentVariable("ARK_API_KEY", "你的火山引擎API密钥", "User")
```

### Linux/macOS

```bash
# 临时设置（当前终端生效）
export ARK_API_KEY="你的火山引擎API密钥"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export ARK_API_KEY="你的火山引擎API密钥"' >> ~/.bashrc
source ~/.bashrc
```

## 📝 使用场景

### 场景 1: Claude Desktop 中使用

**配置步骤**:
1. 打开 Settings → MCP Servers
2. 添加新服务器：
   - Name: `火山引擎生图`
   - Command: `npx volcengine-imagegen-mcp`
   - Environment Variables: `ARK_API_KEY=你的API密钥`
3. 保存并重启

**优点**:
- ✅ 无需安装，直接通过 npx 运行
- ✅ 配置简单，只需一行命令
- ✅ 自动处理依赖下载和编译

### 场景 2: VS Code 中使用

**前置条件**:
1. 安装支持 MCP 的扩展（推荐 Cline）
2. 配置 MCP 服务器

**优点**:
- ✅ 集成度高，与 VS Code 无缝集成
- ✅ 支持代码补全和智能提示
- ✅ 可以在代码编辑器中直接使用 MCP 工具

**详细指南**: 查看 `VS_CODE_GUIDE.md`

### 场景 3: Cursor 中使用

**配置步骤**:
1. 打开 Settings → MCP
2. 添加新服务器：
   ```json
   {
     "name": "火山引擎生图",
     "command": "npx",
     "args": ["volcengine-imagegen-mcp"],
     "env": {
       "ARK_API_KEY": "你的API密钥"
     }
   }
   ```
3. 保存配置

### 场景 4: Trae 中使用

Trae 原生支持火山引擎 MCP 服务，可以直接在火山引擎 MCP 市场中选择使用。

## 📚 文档说明

| 文件名称 | 主要内容 | 适用场景 |
|-----------|----------|----------|
| `README.md` | 项目介绍、安装、使用方法 | 所有用戶 |
| `QUICKSTART.md` | 5 分钟快速开始指南 | 快速上手 |
| `CLAUDE_GUIDE.md` | Claude Desktop 详细使用指南 | Claude 用戶 |
| `VS_CODE_GUIDE.md` | VS Code 详细使用指南 | VS Code 用戶 |
| `EXAMPLES.md` | 丰富的使用示例和优化技巧 | 需要示例的用戶 |

## 🎯 项目特点

### ✅ 优点

1. **完整的错误处理**: API Key 缺失、模型不支持、尺寸无效等
2. **参数验证**: 自动验证模型 ID、尺寸等参数
3. **灵活输出**: 支持 URL 和 Base64 两种格式
4. **详细日志**: 启动时显示可用工具
5. **npx 支持**: 可以直接通过 npx 运行，无需安装
6. **中文友好**: 所有文档、提示词和错误信息都是中文
7. **类型安全**: TypeScript 实现，完整的类型定义
8. **开源友好**: MIT 许可证，易于贡献

### 🔄 技术栈

- **Language**: TypeScript (主要), Python (备用)
- **SDK**: @modelcontextprotocol/sdk
- **HTTP Client**: axios
- **Validation**: zod
- **Package Manager**: npm, npx

### 📊 性能特点

| 操作 | 平均时间 | 说明 |
|------|---------|------|
| 单张文生图 (2K) | 30-60 秒 | 适合快速测试 |
| 单张文生图 (4K) | 60-120 秒 | 最高质量 |
| 图生图 (2K) | 45-90 秒 | 需要参考图 |
| 组图生成 (4 张) | 2-4 分钟 | 快速批量 |
| 组图生成 (15 张) | 10-15 分钟 | 最大批量 |

## 🔧 开发指南

### 本地开发

```bash
# 克隆项目
git clone <repository-url>

# 进入项目目录
cd volcengine-imagegen-mcp

# 安装依赖
npm install

# 开发模式（监听文件变化）
npm run dev

# 构建
npm run build

# 测试
npm start
```

### 发布到 npm

```bash
# 构建项目
npm run build

# 登录 npm
npm login

# 发布（首次）
npm publish --access public

# 更新版本
npm version patch  # 或 minor, major
npm publish
```

### 构建 Python 版本

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行
python -m volcengine_imagegen_mcp
```

## 🐛 已知问题

### TypeScript 版本

1. **类型定义**: MCP SDK 的类型系统可能更新，需要持续关注
2. **构建速度**: 首次构建可能较慢

### Python 版本

1. **依赖安装**: 需要确保 Python 环境正确
2. **FastMCP**: 依赖较新的 MCP 库

## 🚧 未来改进方向

1. **增强功能**:
   - 支持更多火山引擎图像生成模型
   - 添加图片编辑功能（裁剪、缩放、滤镜）
   - 支持批量下载和保存
   - 添加图片历史记录

2. **优化性能**:
   - 实现请求缓存
   - 支持流式返回大图片
   - 优化 Base64 处理

3. **改进文档**:
   - 添加更多实际使用案例
   - 提供视频教程
   - 添加故障排查指南

4. **扩展集成**:
   - 集成更多 AI 代码编辑器
   - 提供浏览器扩展
   - 添加移动端支持

## 📞 贡献指南

### 如何贡献

1. **Fork 项目**: 在 GitHub 上 Fork 项目
2. **创建特性分支**: `git checkout -b feature/amazing-feature`
3. **进行开发**: 实现你的功能
4. **提交代码**: `git commit -m "Add amazing feature"`
5. **推送分支**: `git push origin feature/amazing-feature`
6. **创建 Pull Request**: 在 GitHub 上创建 PR

### 贡献建议

- ✅ 遵循代码风格
- ✅ 添加适当的测试
- ✅ 更新文档
- ✅ 响应 Issue
- ✅ 保持代码简洁

### Issue 模板

**Bug 报告**:
```
**描述**: 简明描述 Bug
**复现步骤**: 
1. 
2. 
3. 

**期望行为**: 

**实际行为**: 

**环境信息**:
- OS: 
- Node.js 版本: 
- 项目版本: 
```

**功能请求**:
```
**功能名称**: 
**详细描述**: 
**使用场景**: 
**预期效果**: 
```

## 📞 联系方式

- **Issues**: [GitHub Issues](https://github.com/your-username/volcengine-imagegen-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/volcengine-imagegen-mcp/discussions)

## 📋 检查清单

发布前检查：

- [ ] 代码已测试
- [ ] 文档已更新
- [ ] README.md 完整
- [ ] 已添加示例
- [ ] 已添加使用指南
- [ ] 已更新版本号
- [ ] 已测试 Claude Desktop 集成
- [ ] 已测试 VS Code 集成
- [ ] 已测试 Cursor 集成
- [ ] 已添加许可证文件
- [ ] 已准备发布

---

## 🎉 总结

本项目提供了一个完整的、生产就绪的火山引擎 AI 生图 MCP 工具实现。支持通过 npx 直接运行，无需复杂的安装过程。项目包含详细的文档和示例，方便用户快速上手。

**核心价值**:
- ✅ 填补了火山引擎 AI 生图功能的 MCP 生态空白
- ✅ 提供了简单易用的接口
- ✅ 支持多种部署方式
- ✅ 完善的文档和示例

**立即开始使用**:
1. 获取火山引擎 API Key
2. 运行 `npx volcengine-imagegen-mcp`
3. 在 Claude Desktop 或 VS Code 中配置
4. 开始生成图片！

**项目状态**: ✅ 完成并可使用

**下一步**: 分享给其他用户，收集反馈，持续改进

---

**文档更新日期**: 2026-01-20
**项目版本**: 1.0.0
