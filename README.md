# 火山引擎 AI 生图 MCP 服务器

基于 npx 的 Model Context Protocol (MCP) 服务器，用于调用火山引擎豆包生图 API。

## ✨ 特性

- 🎨 **文生图**: 根据文本提示词生成图片
- 🖼️ **图生图**: 根据参考图片和文本生成新图片
- 📸 **组图生成**: 生成一组内容关联的图片（最多15张）
- 🎯 **多模型支持**: 支持 doubao-seedream 4.5/4.0/3.0 系列
- 📐 **多尺寸支持**: 2K, 4K, 1024x1024, 2048x2048
- 🔄 **灵活输出**: 支持返回 URL 或 Base64 格式
- 💧 **水印控制**: 可选择是否添加水印

## 📦 安装

### 1. 全局安装（推荐）

```bash
npm install -g volcengine-imagegen-mcp
```

### 2. 使用 npx 运行（无需安装）

```bash
npx volcengine-imagegen-mcp
```

## 🔑 配置 API Key

在使用之前，需要设置火山引擎 API Key：

### Windows

```cmd
set ARK_API_KEY=你的火山引擎API密钥
```

### PowerShell

```powershell
$env:ARK_API_KEY="你的火山引擎API密钥"
```

### Linux/macOS

```bash
export ARK_API_KEY="你的火山引擎API密钥"
```

### 如何获取 API Key？

1. 访问 [火山方舟控制台](https://console.volcengine.com/ark/region:ark+cn-beijing/overview)
2. 登录火山引擎账号
3. 创建 API Key
4. 复制 API Key 并设置环境变量

## 🚀 使用方法

### 在 Claude Desktop 中使用

1. 打开 Claude Desktop 设置
2. 找到 MCP Servers 配置项
3. 添加新服务器：
   - **名称**: `volcengine-imagegen-mcp`
   - **命令**: `npx volcengine-imagegen-mcp`
   - **环境变量**: `ARK_API_KEY=你的API密钥`
4. 保存配置并重启 Claude Desktop

### 在 Cursor 中使用

1. 打开 Cursor 设置
2. 找到 MCP 配置
3. 添加服务器：
   ```json
   {
     "name": "volcengine-imagegen",
     "command": "npx",
     "args": ["volcengine-imagegen-mcp"],
     "env": {
       "ARK_API_KEY": "你的API密钥"
     }
   }
   ```

### 在 Trae 中使用

Trae 原生支持火山引擎 MCP 服务，可以直接在火山引擎 MCP 市场中选择使用。

## 🛠️ 可用工具

### 1. generate_image - 文生图

根据文本提示词生成图片。

**参数**:
- `model` (string): 模型 ID，默认 "doubao-seedream-4.5"
- `prompt` (string): 图片生成提示词（支持中英文）
- `size` (string): 图片尺寸，默认 "2K"（支持：2K, 4K, 1024x1024, 2048x2048）
- `guidance_scale` (number): 文本权重（1-10），默认 2.5
- `response_format` (string): 返回格式，默认 "url"（支持：url, b64_json）
- `watermark` (boolean): 是否添加水印，默认 false
- `count` (number): 生成图片数量（1-4张），默认 1

**示例提示**:
```
生成一张充满活力的特写肖像，模特眼神犀利
```

### 2. image_to_image - 图生图

根据参考图片和文本提示词生成新图片。

**参数**:
- `model` (string): 模型 ID，默认 "doubao-seedream-4.5"
- `prompt` (string): 图片生成提示词
- `image_urls` (array): 参考图片 URL 列表（最多14张）
- `size` (string): 图片尺寸，默认 "2K"
- `guidance_scale` (number): 文本权重（1-10），默认 2.5
- `response_format` (string): 返回格式，默认 "url"
- `watermark` (boolean): 是否添加水印，默认 false

**示例提示**:
```
根据这张图片的风格，生成一张新的城市夜景照片
[上传参考图片]
```

### 3. generate_image_set - 组图生成

生成一组内容关联的图片（最多15张）。

**参数**:
- `model` (string): 模型 ID，默认 "doubao-seedream-4.5"
- `prompt` (string): 图片生成提示词
- `count` (number): 生成图片数量（2-15张），默认 4
- `size` (string): 图片尺寸，默认 "2K"
- `guidance_scale` (number): 文本权重（1-10），默认 2.5
- `response_format` (string): 返回格式，默认 "url"
- `watermark` (boolean): 是否添加水印，默认 false

**示例提示**:
```
生成一组4张科幻风格的太空探索主题插画
```

### 4. list_models - 获取模型列表

获取所有支持的模型及其说明。

## 📋 支持的模型

| 模型 ID | 说明 | 支持的功能 |
|---------|------|-------------|
| `doubao-seedream-4.5` | 豆包生图 4.5（最新） | 文生图、图生图、组图、多图生图 |
| `doubao-seedream-4.0` | 豆包生图 4.0 | 文生图、图生图、组图、多图生图 |
| `doubao-seedream-3.0-t2i` | 豆包生图 3.0 文生图 | 仅文生图 |
| `doubao-seedream-3.0-i2i` | 豆包生图 3.0 图生图 | 仅图生图 |

## ⚙️ 高级配置

### 环境变量

| 变量名 | 说明 | 必需 |
|---------|------|-------|
| `ARK_API_KEY` | 火山引擎 API 密钥 | ✅ 是 |

### 返回格式选择

- **url**: 返回图片下载链接（24小时内有效）
- **b64_json**: 直接返回 Base64 编码的图片数据

**建议**：
- 需要快速预览或嵌入应用 → 使用 `b64_json`
- 需要高质量下载或长期保存 → 使用 `url`

## 🎯 使用建议

### 提示词编写技巧

1. **详细描述**: 包含主体、风格、颜色、构图等要素
2. **中英文混合**: 模型对中英文都有良好理解能力
3. **风格指定**: 明确指定想要的风格（如"写实风格"、"动漫风格"等）
4. **质量关键词**: 添加"高清"、"4K"、"专业"等关键词提升质量

### 参数调优建议

| 参数 | 低值 | 高值 | 效果 |
|------|-------|-------|------|
| `guidance_scale` | 1-3 | 7-10 | 低值更自由创作，高值更严格遵循提示词 |
| `size` | 2K, 1024x1024 | 4K, 2048x2048 | 大尺寸需要更多时间和算力 |

### 成本控制

- 图片链接 **24小时后失效**，请及时下载
- 组图生成（15张）需要较长时间，建议先用少量测试
- 4K 分辨率生成成本高于 2K

## 🔧 开发

### 构建

```bash
npm install
npm run build
```

### 本地运行

```bash
npm run start
```

### 开发模式

```bash
npm run dev
```

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

- 问题反馈: [GitHub Issues](https://github.com/your-username/volcengine-imagegen-mcp/issues)
- 火山引擎文档: https://www.volcengine.com/docs/

## 🔗 相关链接

- [火山引擎 MCP 市场](https://www.volcengine.com/mcp-marketplace)
- [火山方舟控制台](https://console.volcengine.com/ark/)
- [豆包生图 API 文档](https://www.volcengine.com/docs/82379/)
