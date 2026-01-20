# 在 Claude Desktop 中使用火山引擎 AI 生图 MCP 工具

本文档详细说明如何在 Claude Desktop 中使用火山引擎 AI 生图 MCP 工具。

## 📋 前提条件

- ✅ 已获取火山引擎 API Key
- ✅ 已配置环境变量 `ARK_API_KEY`（可选）
- ✅ 已安装 Claude Desktop

---

## 🚀 快速开始（三种方法）

### 方法 1：使用 npx（推荐，无需任何配置）

这是最简单的方式，直接在 Claude Desktop 中添加 npx 命令。

#### 配置步骤：

1. 打开 **Claude Desktop**
2. 进入 **Settings** → **MCP Servers**
3. 点击 **Add Server** 添加新服务器
4. 填写以下信息：

| 配置项 | 值 |
|---------|-----|
| **Name** | 火山引擎生图 |
| **Command** | `npx` |
| **Arguments** | `volcengine-imagegen-mcp` |
| **Environment Variables** | `ARK_API_KEY=你的火山引擎API密钥` |

5. 点击 **Save** 保存配置
6. 重启 Claude Desktop

#### 验证是否成功：

重启后，在 Claude 对话中输入：
```
列出所有支持的模型
```

如果看到模型列表，说明配置成功！

---

### 方法 2：使用预编译版本（需要先构建）

如果不想每次都编译，可以先构建项目然后使用编译后的文件。

#### 1. 构建项目

```bash
cd "d:\程序\workspace\opensource\volcengine-imagegen-mcp"
npm run build
```

#### 2. 在 Claude Desktop 中配置

| 配置项 | 值 |
|---------|-----|
| **Name** | 火山引擎生图 |
| **Command** | `node` |
| **Arguments** | `["d:\\程序\\workspace\\opensource\\volcengine-imagegen-mcp\\dist\\index.js"]` |
| **Environment Variables** | `ARK_API_KEY=你的火山引擎API密钥` |

#### 注意事项：

- 确保 `dist/index.js` 文件路径正确
- 每次修改代码后需要重新构建
- 需要手动管理环境变量（推荐使用方法 1）

---

### 方法 3：使用全局安装版本（需要先全局安装）

#### 1. 全局安装

```bash
npm install -g volcengine-imagegen-mcp
```

#### 2. 在 Claude Desktop 中配置

| 配置项 | 值 |
|---------|-----|
| **Name** | 火山引擎生图 |
| **Command** | `volcengine-imagegen-mcp` |
| **Arguments** | （留空） |
| **Environment Variables** | `ARK_API_KEY=你的火山引擎API密钥` |

---

## 🛠️ 可用工具列表

在 Claude Desktop 中配置成功后，你可以使用以下 4 个工具：

| 工具名称 | 功能 | 支持模型 | 关键参数 |
|-----------|------|-----------|-----------|
| `generate_image` | 文生图 | doubao-seedream-4.5/4.0/3.0-t2i/i2i | prompt, size, count, guidance_scale, response_format, watermark |
| `image_to_image` | 图生图 | doubao-seedream-4.5/4.0 | prompt, image_urls, size, guidance_scale, response_format, watermark |
| `generate_image_set` | 组图生成（最多 15 张） | doubao-seedream-4.5/4.0 | prompt, count, size, guidance_scale, response_format, watermark |
| `list_models` | 获取模型列表 | - | - |

---

## 💡 使用示例

### 示例 1：生成单张图片（文生图）

**在 Claude 中输入**：
```
生成一张充满活力的特写肖像，模特眼神犀利，4K 分辨率
```

**Claude 会自动调用**：
- 工具：`generate_image`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "充满活力的特写肖像，模特眼神犀利",
    "size": "4K",
    "count": 1
  }
  ```

**预期结果**：
- 生成 1 张 4K 分辨率的特写肖像
- 返回图片下载链接

---

### 示例 2：生成多张图片（批量生成）

**在 Claude 中输入**：
```
生成 3 张不同风格的城市夜景，使用 doubao-seedream-4.5 模型，2K 分辨率
```

**Claude 会自动调用**：
- 工具：`generate_image`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "不同风格的城市夜景",
    "size": "2K",
    "count": 3
  }
  ```

**预期结果**：
- 生成 3 张 2K 分辨率的城市夜景
- 每张都是不同风格

---

### 示例 3：图生图

**前提**：需要先有参考图片（可以上传到网上或通过其他方式获得 URL）

**在 Claude 中输入**：
```
根据这张图片的风格，生成一张新的商务肖像，背景简洁专业
```

**Claude 会询问**：
```
请提供参考图片的 URL（最多 14 张）
```

**提供 URL 后**：
- 工具：`image_to_image`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "根据这张图片的风格，生成一张新的商务肖像，背景简洁专业",
    "image_urls": ["https://example.com/reference.jpg"]
  }
  ```

**预期结果**：
- 根据参考图生成新图片
- 保持原图的商务风格

---

### 示例 4：组图生成

**在 Claude 中输入**：
```
生成一组 6 张科幻风格的太空探索主题插画，内容连贯
```

**Claude 会自动调用**：
- 工具：`generate_image_set`
- 参数：
  ```json
  {
    "model": "doubao-seedream-4.5",
    "prompt": "科幻风格的太空探索主题插画，内容连贯",
    "count": 6,
    "size": "2K"
  }
  ```

**预期结果**：
- 生成 6 张内容关联的科幻插画
- 可以用于漫画、小说配图等

---

### 示例 5：查看支持的模型

**在 Claude 中输入**：
```
列出所有支持的模型和它们的功能
```

**Claude 会调用**：
- 工具：`list_models`
- 返回：所有模型的详细信息

**预期结果**：
显示模型列表，包括：
- doubao-seedream-4.5：支持文生图、图生图、组图、多图生图
- doubao-seedream-4.0：支持文生图、图生图、组图、多图生图
- doubao-seedream-3.0-t2i：仅支持文生图
- doubao-seedream-3.0-i2i：仅支持图生图

---

## 🎯 提示词优化建议

### 中文提示词示例

为了让 Claude 生成更好的图片，可以使用以下提示词风格：

#### 肖像类
```
专业摄影师拍摄的商业肖像，自然光，眼神自信，背景简洁虚化突出主体，柔和光效，细节丰富
```

#### 风景类
```
一幅美丽的山水风景画，云雾缭绕，阳光穿透云层，形成丁达尔光效，色彩层次丰富
```

#### 插画类
```
日式动漫风格插画，精细线条，鲜艳色彩，柔和光影，治愈系风格，适合轻小说配图
```

#### 抽象艺术
```
超现实主义风格，几何形状组合，梦幻光影效果，色彩丰富，渐变自然，现代艺术风格
```

### 英文提示词示例

```
Photorealistic portrait, natural lighting, confident eyes, blurred background, soft lighting, rich details
Anime style illustration, clean lines, vibrant colors, gentle lighting, healing vibe, suitable for light novel illustrations
Cyberpunk aesthetic, neon lighting effects, futuristic elements, dark atmosphere, holographic effects
```

---

## ⚙️ 参数调优指南

### 尺寸选择建议

| 使用场景 | 推荐尺寸 | 预期时间 | 质量 |
|-----------|-----------|---------|------|
| 快速测试/预览 | `2K` 或 `1024x1024` | 30-60 秒 | 足够快速查看 |
| 平衡质量 | `2K` 或 `2048x2048` | 60-90 秒 | 良好平衡 |
| 最高质量 | `4K` | 90-120 秒 | 专业级输出 |

### 文本权重（guidance_scale）调优

| 数值 | 效果说明 | 适用场景 |
|------|---------|---------|
| `1.0-3.0` | 更自由的创作，图片更有创意性 | 艺术创作、风格探索 |
| `4.0-6.0` | 平衡创意和提示词遵循 | 日常使用 |
| `7.0-10.0` | 严格遵循提示词，细节准确 | 商业需求、精确控制 |

### 返回格式选择

| 格式 | 优点 | 缺点 | 适用场景 |
|------|------|-------|---------|
| `url` | 下载速度快，可直接保存 | 链接 24 小时后失效 |
| `b64_json` | 直接获取图片数据，可嵌入代码 | 数据量大时可能影响性能 |

---

## 🔧 高级使用技巧

### 技巧 1：渐进式生成

从简单开始，逐步增加复杂度：

1. **第一轮**：简单提示词 + 低文本权重
   ```
   一只可爱的猫
   ```

2. **第二轮**：添加细节
   ```
   一只毛茸茸的橘色小猫，坐在阳光下
   ```

3. **第三轮**：调整风格
   ```
   一只毛茸茸的橘色小猫，坐在阳光下，日式动漫风格
   ```

### 技巧 2：利用 Claude 的多轮对话

Claude 可以记住对话上下文，可以利用这一点：

```
你：生成一张城市夜景
Claude: [生成图片]

你：调整光线为黄金时刻的暖色调
Claude: [基于刚才的图片生成，调整光线]

你：改变为赛博朋克风格
Claude: [基于前面的风格，生成赛博朋克版本]
```

### 技巧 3：混合使用工具

结合不同的工具达到更好的效果：

1. 先用 `generate_image` 生成基础图片
2. 再用 `image_to_image` 基于基础图生成变体
3. 对比选择最好的版本

---

## ⚠️ 注意事项

### API Key 安全

- ❌ **不要**将 API Key 提交到 GitHub 或公开分享
- ✅ **务必**只在 Claude Desktop 配置中填写
- ✅ **建议**定期更换 API Key

### 图片链接时效

- 生成的图片链接 **24 小时后失效**
- 需要及时下载或使用 `response_format: "b64_json"` 直接获取数据
- 重要图片建议使用 Base64 格式

### 模型选择

- `doubao-seedream-4.5`：最新模型，支持所有功能（推荐）
- `doubao-seedream-4.0`：稳定模型，支持大部分功能
- `doubao-seedream-3.0-t2i`：仅支持文生图
- `doubao-seedream-3.0-i2i`：仅支持图生图

### 成本控制

- `4K` 分辨率生成成本是 `2K` 的约 2-4 倍
- 组图生成（15 张）需要较长时间（10-15 分钟）
- 建议先用小批量测试，满意后再批量生成

---

## 🚨 故障排查

### 问题：Claude 无法调用 MCP 工具

**检查清单**：
1. ✅ Claude Desktop 是否已重启？
2. ✅ MCP Server 配置是否保存？
3. ✅ API Key 是否正确？
4. ✅ 命令参数是否正确？

**解决方案**：
- 重新启动 Claude Desktop
- 删除并重新添加 MCP Server
- 检查 Claude Desktop 的日志（设置中可查看）

### 问题：调用失败或返回错误

**常见错误**：
- `❌ 错误：未设置 ARK_API_KEY 环境变量`
  - 解决方案：在 Claude Desktop 的 MCP Server 配置中添加环境变量
- `❌ 错误：不支持的模型 "xxx"`
  - 解决方案：使用 `list_models` 工具查看支持的模型
- `❌ 错误：不支持的尺寸 "xxx"`
  - 解决方案：使用 2K、4K、1024x1024、2048x2048 之一
- `❌ API 调用失败：xxx`
  - 解决方案：检查 API Key 是否有效，网络连接是否正常

---

## 📊 性能参考

### 单张图片生成时间

| 分辨率 | 平均时间 | 模型 |
|--------|---------|------|
| 1024x1024 | 30-45 秒 | doubao-seedream-4.5 |
| 2K | 45-90 秒 | doubao-seedream-4.5 |
| 4K | 90-180 秒 | doubao-seedream-4.5 |

### 组图生成时间

| 图片数量 | 平均时间 | 说明 |
|---------|---------|------|
| 4 张 | 3-5 分钟 | 快速批量 |
| 8 张 | 6-10 分钟 | 中等批量 |
| 15 张 | 12-20 分钟 | 最大批量 |

---

## 💡 最佳实践

### 1. 提示词编写

- ✅ 使用描述性语言（如"一只毛茸茸的橘色小猫"）
- ✅ 包含关键元素（主体、风格、光线、背景、颜色）
- ✅ 指定技术细节（"8K 分辨率"、"专业摄影质量"）
- ✅ 中英文混用（模型对两种语言都有理解）

### 2. 参数优化

- ✅ 从低分辨率（2K）开始测试
- ✅ 逐步调整 `guidance_scale` 参数
- ✅ 测试不同 `size` 参数找到最佳平衡点

### 3. 工作流程

- ✅ 先用 `list_models` 了解可用模型
- ✅ 用简单提示词测试基本功能
- ✅ 逐步增加提示词复杂度
- ✅ 满意后使用 `b64_json` 格式保存重要图片

### 4. 成本管理

- ✅ 避免频繁使用 4K 分辨率
- ✅ 合理使用批量生成功能
- ✅ 及时下载图片（URL 格式 24 小时失效）

---

## 🎨 创意项目示例

### 项目 1：生成漫画分镜

```
第 1 页：主角在城市街头的特写
第 2 页：主角走进一家咖啡馆
第 3 页：咖啡馆内部温馨场景
第 4 页：主角点了一杯咖啡，窗外风景
```

**实现方式**：
1. 使用 `generate_image`，count=4，生成 4 张
2. 每张描述一个分镜场景
3. 后续可以用 `image_to_image` 调整风格

### 项目 2：产品展示图

```
生成一组产品图片：
- 正面展示（白背景）
- 侧面展示（45 度角）
- 使用场景（放在桌面上）
- 特写细节（按钮、材质）
```

**实现方式**：
1. 使用 `generate_image_set`，count=6，一次生成
2. 统一风格和光线
3. 使用 `response_format: "b64_json"` 方便嵌入网站

### 项目 3：社交媒体配图

```
生成一系列社交媒体配图：
- 头像（圆形裁剪）
- 封面图（带标题空间）
- 背景图（适合帖子）
- 表情包（卡通风格）
```

**实现方式**：
1. 分批生成（每批 4-6 张）
2. 测试不同风格找到最佳方案
3. 使用 2K 分辨率平衡质量和速度

---

## 📞 相关资源

- [Claude Desktop 下载](https://claude.ai/download)
- [火山方舟控制台](https://console.volcengine.com/ark/)
- [火山引擎 API 文档](https://www.volcengine.com/docs/82379/)
- [MCP 协议规范](https://modelcontextprotocol.io/)

---

## ✅ 检查清单

使用前确认以下事项：

- [ ] 已获取火山引擎 API Key
- [ ] 已在 Claude Desktop 中添加 MCP Server
- [ ] 已测试基本功能（如生成单张图片）
- [ ] 已了解可用工具和参数
- [ ] 已阅读提示词优化建议
- [ ] 已了解成本和性能参考

---

**祝你使用愉快！如有问题，请查看 VS_CODE_GUIDE.md 了解如何在 VS Code 中使用此工具。** 🎉
