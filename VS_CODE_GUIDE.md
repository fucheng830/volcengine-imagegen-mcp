# 在 VS Code 中使用火山引擎 AI 生图 MCP 工具

本文档详细说明如何在 VS Code 中使用火山引擎 AI 生图 MCP 工具。

## 📋 前提条件

1. ✅ 已安装 VS Code
2. ✅ 已安装 MCP 扩展（支持 MCP 协议的 VS Code 扩展）
3. ✅ 已获取火山引擎 API Key

## 🔑 第一步：获取火山引擎 API Key

### 1.1 访问火山方舟控制台

1. 打开浏览器，访问：https://console.volcengine.com/ark/region:ark+cn-beijing/overview
2. 使用火山引擎账号登录
3. 进入「API Key 管理」页面
4. 点击「创建 API Key」
5. 选择合适的权限（建议选择「全选」或至少包含「图片生成」权限）
6. 点击「确认」创建
7. **复制 API Key**（后续会用到）

### 1.2 本地配置 API Key（推荐）

**Windows PowerShell**:
```powershell
# 临时设置（当前窗口生效）
$env:ARK_API_KEY="你的API密钥"

# 持久化设置（写入用户环境变量）
[System.Environment]::SetEnvironmentVariable("ARK_API_KEY", "你的API密钥", "User")
```

**Windows CMD**:
```cmd
REM 临时设置
set ARK_API_KEY=你的API密钥

REM 持久化设置（需要管理员权限）
setx ARK_API_KEY "你的API密钥"
```

**Linux/macOS**:
```bash
# 临时设置（当前终端生效）
export ARK_API_KEY="你的API密钥"

# 持久化设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export ARK_API_KEY="你的API密钥"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🔌 第二步：安装支持 MCP 的 VS Code 扩展

### 方案 1：安装 Cline（推荐）

**Cline** 是目前最流行、最稳定的 VS Code MCP 扩展。

1. 打开 VS Code
2. 点击左侧「扩展」图标（或按 `Ctrl+Shift+X`）
3. 在搜索框中输入 `Cline`
4. 找到由 **Allan Branch** 开发的「Cline」扩展
5. 点击「安装」

### 方案 2：安装 Continue

**Continue** 也是流行的 VS Code MCP 扩展。

1. 在 VS Code 扩展市场中搜索 `Continue`
2. 安装由 **Continue Dev Inc** 开发的扩展
3. 安装后重启 VS Code

### 方案 3：安装其他支持 MCP 的扩展

其他支持 MCP 协议的扩展：
- **Rooster** - 由 OpenRouter 开发
- **Roo Code** - 由 JetBrains 开发

---

## ⚙️ 第三步：配置 VS Code MCP 扩展

以下以 **Cline** 为例，其他扩展的配置方法类似。

### 3.1 打开 MCP 配置

1. 按 `Ctrl+,`（逗号）打开 VS Code 设置
2. 搜索 `mcp` 或 `MCP`
3. 找到「MCP Servers」或类似配置项

### 3.2 添加火山引擎 MCP 服务器

在 MCP Servers 配置中点击「Add Server」或「+」，填入以下信息：

#### 配置信息（选择其一）：

**方案 A：使用 npx（推荐，无需编译）**
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

**方案 B：使用本地编译（需先构建）**

1. 先编译项目：
```bash
cd "d:\程序\workspace\opensource\volcengine-imagegen-mcp"
npm run build
```

2. 添加配置：
```json
{
  "name": "火山引擎生图",
  "command": "node",
  "args": ["d:\\程序\\workspace\\opensource\\volcengine-imagegen-mcp\\dist\\index.js"],
  "env": {
    "ARK_API_KEY": "你的API密钥"
  }
}
```

**方案 C：使用 Python 版本**

如果已安装 Python：
```json
{
  "name": "火山引擎生图-Python",
  "command": "python",
  "args": ["-m", "volcengine_imagegen_mcp", "d:\\程序\\workspace\\opensource\\volcengine-imagegen-mcp\\server.py"],
  "env": {
    "ARK_API_KEY": "你的API密钥"
  }
}
```

### 3.3 保存配置

点击「Save」或「Apply」保存配置。

---

## 🚀 第四步：在 VS Code 中使用

### 4.1 打开聊天界面

1. 在 VS Code 侧边栏找到 MCP 扩展的图标（如 Cline 图标）
2. 点击打开聊天面板

### 4.2 调用 MCP 工具

在聊天框中输入提示词，例如：

```
生成一张充满活力的特写肖像，模特眼神犀利，4K分辨率
```

MCP 扩展会自动调用火山引擎的 `generate_image` 工具。

### 4.3 查看可用工具

在 VS Code 中，你通常会看到以下 MCP 工具可用：

- **generate_image** - 文生图
- **image_to_image** - 图生图
- **generate_image_set** - 组图生成
- **list_models** - 获取模型列表

---

## 💡 使用示例

### 示例 1：生成单张图片

**VS Code 聊天输入**:
```
生成一张日式动漫风格的城市夜景图，霓虹灯闪烁，赛博朋克风格
```

**MCP 会自动调用**:
- 工具：`generate_image`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "日式动漫风格的城市夜景图，霓虹灯闪烁，赛博朋克风格",
    "size": "2K",
    "count": 1
  }
  ```

**预期结果**:
- 生成 1 张 2K 分辨率的日式动漫风格赛博朋克城市夜景
- 返回图片下载链接

---

### 示例 2：生成多张图片

**VS Code 聊天输入**:
```
生成4张不同风格的自然风景画：春天樱花盛开、夏天海滩日落、秋天枫叶飘零、冬天雪景纷飞，每张都要高清质量
```

**MCP 会自动调用**:
- 工具：`generate_image`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "春天樱花盛开、夏天海滩日落、秋天枫叶飘零、冬天雪景纷飞，每张都要高清质量",
    "size": "2K",
    "count": 4
  }
  ```

**预期结果**:
- 生成 4 张不同季节的自然风景画
- 每张都是 2K 分辨率

---

### 示例 3：图生图

**前提**: 需要先上传一张参考图片到 VS Code 工作区或通过 URL 访问

**VS Code 聊天输入**:
```
根据这张照片的风格，生成一张新的商务肖像，背景简洁专业
```

**MCP 会自动调用**:
- 工具：`image_to_image`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "根据这张照片的风格，生成一张新的商务肖像，背景简洁专业",
    "image_urls": ["https://example.com/reference.jpg"],
    "size": "2K"
  }
  ```

---

### 示例 4：组图生成

**VS Code 聊天输入**:
```
生成一组6张连续的科幻主题插画，展现从城市到太空的探索历程
```

**MCP 会自动调用**:
- 工具：`generate_image_set`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "展现从城市到太空的探索历程",
    "count": 6,
    "size": "2K"
  }
  ```

---

### 示例 5：查看支持的模型

**VS Code 聊天输入**:
```
列出所有支持的模型和它们的功能
```

**MCP 会自动调用**:
- 工具：`list_models`
- 返回模型列表和说明

---

### 示例 6：生成 Base64 格式（用于嵌入）

**VS Code 聊天输入**:
```
生成一张简约风格的企业 Logo 设计，以 Base64 格式返回，方便直接嵌入 HTML
```

**MCP 会自动调用**:
- 工具：`generate_image`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "简约风格的企业 Logo 设计，以 Base64 格式返回，方便直接嵌入 HTML",
    "response_format": "b64_json",
    "size": "1024x1024"
  }
  ```

**预期结果**:
- 直接返回 Base64 编码的图片数据
- 可以在 VS Code 中预览或复制使用

---

## 🎯 高级使用技巧

### 技巧 1：优化提示词

**详细描述** = 更好的生成效果

❌ 简单: "一只猫"
✅ 详细: "一只毛茸茸的橘色小猫，坐在阳光下，毛发闪闪发光，眼神温暖好奇，背景是绿草地和蓝天，细节丰富，光影效果出色"

### 技巧 2：使用中文提示词

火山引擎豆包生图对中英文都有良好理解：

```
一张充满活力的特写肖像，模特眼神犀利
```

对比

```
充满活力的特写肖像，模特眼神犀利
```

中文提示词会生成更符合中文语境的图片。

### 技巧 3：调整参数

**尺寸选择**:
- **快速测试**: `2K` 或 `1024x1024`（约 30-60 秒）
- **平衡质量**: `2048x2048`（约 60-120 秒）
- **最高质量**: `4K`（约 60-120 秒）

**文本权重**:
- **创意自由**: `1.0` - `3.0`
- **平衡**: `2.5` - `5.0`
- **严格遵循**: `6.0` - `10.0`

---

## ⚙️ 故障排查

### 问题 1: VS Code 无法识别 MCP 服务器

**可能原因**:
- API Key 未设置
- 路径配置错误
- 扩展版本过旧

**解决方案**:
1. 检查 API Key 是否正确设置
2. 验证配置中的路径是否正确
3. 更新 VS Code 和 MCP 扩展到最新版本

### 问题 2: 调用失败

**错误信息示例**:
```
❌ 错误：未设置 ARK_API_KEY 环境变量。
```

**解决方案**:
按照「第一部分：获取火山引擎 API Key」中的步骤设置环境变量

### 问题 3: 生成的图片无法查看

**如果使用 URL 格式**:
- 图片链接 24 小时后失效
- 需要手动下载

**解决方案**:
- 使用 `response_format: "b64_json"` 参数直接获取图片数据
- 在 VS Code 中右键点击图片链接，选择「在浏览器中打开」

---

## 📚 参考资料

- [VS Code 官方下载](https://code.visualstudio.com/)
- [Cline 扩展文档](https://github.com/allanbran/cline)
- [Continue 扩展文档](https://github.com/continuedev/continue)
- [MCP 协议规范](https://modelcontextprotocol.io/)
- [火山引擎 API 文档](https://www.volcengine.com/docs/82379/)
- [火山方舟控制台](https://console.volcengine.com/ark/)

---

## 🎨 创意工作流建议

### 工作流 1: 生成多个版本选优

1. 固定提示词，调整 `guidance_scale` 从 2.0 到 8.0
2. 对比生成的图片，选择最佳版本
3. 基于最佳版本，微调提示词再次生成

### 工作流 2: 风格探索

1. 使用相同提示词，但添加不同风格关键词
2. 对比生成效果，记录最满意的风格
3. 形成自己的"风格词库"供后续使用

### 工作流 3: 组图 + 单图混合

1. 先使用 `generate_image_set` 生成一组基础图片
2. 使用 `image_to_image` 基于某张图片生成变体
3. 选择最佳组合用于项目

---

## ✅ 检查清单

使用前确认：

- [ ] 已获取火山引擎 API Key
- [ ] 已在本地或环境变量中设置 API Key
- [ ] 已安装支持 MCP 的 VS Code 扩展（如 Cline）
- [ ] 已在 VS Code 中配置 MCP 服务器
- [ ] API Key 已填入配置
- [ ] 已测试基本功能（如生成单张图片）

---

## 💡 小贴士

1. **首次使用建议**: 从简单的文生图开始，熟悉工具调用方式
2. **成本控制**: 4K 分辨率成本较高，建议先用 2K 测试
3. **及时保存**: URL 链接 24 小时后失效，生成的满意图片请及时下载
4. **参数优化**: 详细的提示词和合适的参数组合能显著提升生成质量
5. **批量生成**: 组图生成功能可以一次性生成多张相关图片，提高效率

---

**祝你使用愉快！如有问题，请查看 README.md 获取更多帮助。** 🎉
