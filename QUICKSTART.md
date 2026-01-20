# 🚀 快速开始指南

欢迎使用火山引擎 AI 生图 MCP 工具！本指南将帮助你在 5 分钟内开始使用。

---

## 📋 步骤 1：获取 API Key（1 分钟）

### 1.1 访问火山方舟控制台

点击以下链接访问：
https://console.volcengine.com/ark/region:ark+cn-beijing/overview

### 1.2 创建 API Key

1. 登录火山引擎账号
2. 进入「API Key 管理」页面
3. 点击「创建 API Key」
4. 选择权限：选择「图片生成」或「全选」
5. 点击「确认」创建
6. **复制 API Key**（后面会用到）

---

## 🔑 步骤 2：配置 API Key（1 分钟）

### Windows 用户

```cmd
REM 临时设置（当前窗口有效）
set ARK_API_KEY=你的API密钥
```

### macOS/Linux 用户

```bash
export ARK_API_KEY="你的API密钥"
```

**重要**：
- 如果在 VS Code 或 Claude Desktop 中配置，可以**跳过此步骤**，直接在 MCP Server 配置中设置环境变量
- 如果要持久化，请修改系统环境变量

---

## 💻 步骤 3：在 Claude Desktop 中使用（2 分钟）

### 3.1 安装 Claude Desktop

如果还没有安装，访问：https://claude.ai/download

### 3.2 配置 MCP Server

1. 打开 Claude Desktop
2. 点击 **Settings**（或按 `Ctrl+,` 打开设置）
3. 找到 **MCP Servers** 或 **MCP 配置**
4. 点击 **Add Server** 或 **+** 添加服务器

### 3.3 填入配置信息

| 配置项 | 值 |
|---------|-----|
| **Name** | `火山引擎生图`（或你喜欢的名称） |
| **Command** | `npx` |
| **Arguments** | `volcengine-imagegen-mcp` |
| **Environment Variables** | `ARK_API_KEY=你的API密钥` |

**示例**：
```
Name: 火山引擎生图
Command: npx
Arguments: volcengine-imagegen-mcp
Environment Variables: ARK_API_KEY=ark-xxxxxxxxxxxx
```

### 3.4 保存并重启

1. 点击 **Save** 或 **Apply**
2. **重启 Claude Desktop**

---

## 🎉 步骤 4：开始使用（1 分钟）

### 验证配置是否成功

在 Claude 对话框中输入：
```
列出所有支持的模型
```

如果看到模型列表说明配置成功！

### 第一次使用建议

#### 测试文生图

在 Claude 中输入：
```
生成一张可爱的橘色小猫，坐在阳光下，毛发闪闪发光
```

**预期结果**：
- 生成 1 张 2K 分辨率的橘色小猫图片
- 返回图片下载链接

#### 查看模型列表

在 Claude 中输入：
```
列出所有支持的模型
```

**预期结果**：
- 显示所有可用模型及其功能
- 了解不同模型的支持情况

---

## 💻 步骤 3：在 VS Code 中使用（2 分钟）

### 3.1 安装支持 MCP 的扩展

推荐安装 **Cline** 扩展：

1. 打开 VS Code
2. 点击左侧「扩展」图标（或按 `Ctrl+Shift+X`）
3. 在搜索框中输入：`Cline`
4. 找到由 **Allan Branch** 开发的「Cline」扩展
5. 点击「安装」

**其他选择**：
- **Continue** - 也是流行的 VS Code MCP 扩展

### 3.2 配置 MCP Server

1. 按 `Ctrl+,` 打开 VS Code 设置
2. 搜索 `MCP` 或找到「MCP Servers」配置
3. 点击「Add Server」或「+」添加服务器

### 3.3 填入配置信息

| 配置项 | 值 |
|---------|-----|
| **Name** | `火山引擎生图` |
| **Command** | `npx` |
| **Arguments** | `volcengine-imagegen-mcp` |
| **Environment Variables** | `ARK_API_KEY=你的API密钥` |

### 3.4 保存并重新加载窗口

1. 点击 **Save」或「Apply」
2. VS Code 会自动重新加载 MCP 服务器

---

## 🚀 步骤 4：开始使用（1 分钟）

### 验证配置是否成功

打开 VS Code 的 AI 聊天面板（或使用 Cline 的聊天界面），输入：
```
列出所有支持的模型
```

如果看到模型列表说明配置成功！

### 第一次使用建议

#### 测试文生图

在 VS Code 聊天框中输入：
```
生成一张日式动漫风格的城市夜景，霓虹灯闪烁，赛博朋克风格
```

**预期结果**：
- 生成 1 张 2K 分辨率的日式动漫风格城市夜景
- 返回图片下载链接

#### 查看模型列表

```
列出所有支持的模型
```

---

## 🎨 进阶使用技巧

### 技巧 1：优化提示词

#### ❌ 糟糕的提示词
```
一只猫
```

#### ✅ 优秀的提示词
```
一只毛茸茸的橘色小猫，坐在阳光下，毛发闪闪发光，眼神温暖好奇，背景是绿草地和蓝天，细节丰富，光影效果出色，专业摄影质量
```

**对比**：
- ❌ 太简单，不知道要什么样的猫、什么样的背景、什么样的光线
- ✅ 详细描述：橘色、毛茸茸、阳光下、毛发闪发光、眼神温暖好奇、绿草地蓝天、细节丰富、光影效果出色、专业摄影质量

### 技巧 2：多轮对话优化

Claude 支持多轮对话，可以利用这个特性：

```
你：生成一张城市夜景
Claude: [生成图片]

你：调整光线为黄金时刻的暖色调
Claude: [基于刚才的图片，生成新版本，调整光线]
```

**优势**：
- 不用一次性写完美的提示词
- 可以根据结果逐步优化
- 更容易找到满意的输出

### 技巧 3：使用 Base64 格式

如果需要直接嵌入图片（如在 HTML 或 Markdown 中），使用 `response_format: "b64_json"` 参数：

```
生成一张简约风格的企业 Logo，以 Base64 格式返回
```

**优势**：
- 直接获取图片数据
- 可以在 VS Code 中预览
- 不需要额外的下载步骤

---

## 📊 快速参考卡

### 常用命令和参数

| 功能 | 提示词示例 | 关键参数 |
|------|-------------|----------|
| **文生图（快速）** | `一只可爱的狗` | model=doubao-seedream-4.5, size=2K |
| **文生图（高质量）** | `专业摄影师拍摄的肖像，8K 分辨率，自然光` | model=doubao-seedream-4.5, size=4K |
| **多张生成** | `4张不同季节的风景` | count=4 |
| **图生图** | `根据参考图生成新版本` | image_urls=[...] |
| **组图生成** | `6张科幻风格插画` | count=6 |

---

## ⚠️ 常见问题

### Q1: 提示"未设置 ARK_API_KEY"错误

**A**: 检查是否设置了环境变量
**B**: 如果在 Claude Desktop 中，检查 MCP Server 配置中的 Environment Variables 是否包含 `ARK_API_KEY`
**C**: 如果在 VS Code 中，检查配置是否正确

### Q2: 生成的图片链接无法打开

**A**: 检查网络连接是否正常
**B**: 尝试在浏览器中打开链接
**C**: 使用 `response_format: "b64_json"` 参数直接获取图片数据

### Q3: 生成速度很慢

**A**: 降低分辨率（使用 2K 而不是 4K）
**B**: 减少图片数量（count=1）
**C**: 选择更简单的提示词

### Q4: VS Code 无法识别 MCP Server

**A**: 确认是否安装了支持 MCP 的扩展（如 Cline）
**B**: 检查配置信息是否正确
**C**: 尝试重启 VS Code
**D**: 查看 VS Code 的开发者工具 → 输出日志

---

## 📞 下一步学习

恭喜你完成了快速开始！接下来你可以：

1. **阅读详细文档**：
   - `README.md` - 完整的项目文档
   - `EXAMPLES.md` - 丰富的使用示例
   - `CLAUDE_GUIDE.md` - Claude Desktop 详细使用指南
   - `VS_CODE_GUIDE.md` - VS Code 详细使用指南

2. **探索更多功能**：
   - 尝试不同的模型（doubao-seedream-4.5 vs 4.0）
   - 调整参数（guidance_scale、size）
   - 使用图生图和组图生成

3. **创建项目**：
   - 为你的工作流准备提示词模板
   - 记录有效的参数组合

---

## 💡 小贴士

- 💡 **快速测试**: 先用简单的提示词测试，确保配置正确
- 💡 **成本控制**: 4K 分辨率成本较高，建议先用 2K 测试
- 💡 **及时保存**: 图片链接 24 小时后失效，重要的图片请及时下载
- 💡 **使用 Base64**: 如果需要嵌入图片，使用 `response_format: "b64_json"`
- 💡 **多轮对话**: 利用 Claude 的记忆功能逐步优化提示词

---

**有问题？查看文档或提交 Issue：**

- 详细文档：查看项目目录中的 README.md
- 问题反馈：[GitHub Issues](https://github.com/your-username/volcengine-imagegen-mcp/issues)

**祝你使用愉快！** 🎉
