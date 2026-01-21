# 火山引擎 AI 生图 MCP 服务器 - 测试指南

本文档提供了所有 MCP 工具的详细测试用例和验证方法。

## 🧪 测试准备

### 测试前检查清单

在使用测试用例之前，请确认：

- [ ] 已安装 Node.js (建议 18+)
- [ ] 已获取火山引擎 API Key
- [ ] 已配置环境变量 `ARK_API_KEY`
- [ ] 已构建项目：`npm run build`
- [ ] 已启动 MCP 服务器（在 Claude Desktop 或 VS Code 中）

### 测试环境说明

- **Claude Desktop**: 直接在对话中使用 MCP 工具
- **VS Code**: 需要先安装支持 MCP 的扩展（如 Cline）
- **Cursor**: 原生支持 MCP 协议

---

## ✅ 测试用例 1: 基本文生图 - 简单测试

### 目的
验证基本的文生图功能是否正常工作

### 测试步骤

1. **在 Claude Desktop 中输入**：
```
生成一张简单的风景画，描绘宁静的湖泊和远山
```

2. **预期行为**：
- Claude 应自动调用 `generate_image` 工具
- 传递参数：`prompt="简单的风景画，湖泊和远山"`, `model="doubao-seedream-4.5"`, `size="2K"`, `count=1`
- API 返回 1 张 2K 分辨率的图片
- Claude 显示图片下载链接

3. **验证点**：
- ✅ 成功生成 1 张图片
- ✅ 返回图片下载链接（24 小时内有效）
- ✅ 显示成功消息
- ✅ 错误处理正常（如果 API Key 无效会显示错误）

### 预期输出示例

```
✅ 成功生成 1 张图片！

**模型**: doubao-seedream-4.5
**提示词**: 简单的风景画，湖泊和远山
**尺寸**: 2K
**文本权重**: 2.5

**图片链接**:
1. https://ark-cn-beijing.volces.com/images/xxx.jpg

⚠️ 注意：图片链接 24 小时后失效，请及时下载。
```

### 预期时间
- API 响应时间：15-30 秒
- Claude 处理时间：1-3 秒

---

## ✅ 测试用例 2: 文生图 - 完整参数测试

### 目的
验证所有参数是否正常工作

### 测试步骤

1. **在 Claude Desktop 中输入**：
```
生成一张专业摄影师拍摄的人像，使用 4K 分辨率，文本权重 7.5，添加水印
```

2. **预期行为**：
- Claude 自动调用 `generate_image` 工具
- 参数：`prompt="专业摄影师拍摄的人像"`, `model="doubao-seedream-4.5"`, `size="4K"`, `guidance_scale=7.5`, `watermark=true`, `count=1`
- 生成 4K 高清人像
- 添加火山引擎水印

3. **验证点**：
- ✅ 成功生成 1 张 4K 分辨率图片
- ✅ 水印功能正常工作
- ✅ 高文本权重（7.5）效果：更严格遵循提示词

### 预期输出示例

```
✅ 成功生成 1 张图片！

**模型**: doubao-seedream-4.5
**提示词**: 专业摄影师拍摄的人像
**尺寸**: 4K
**文本权重**: 7.5
**水印**: 是

**图片链接**:
1. https://ark-cn-beijing.volces.com/images/xxx.jpg

⚠️ 注意：图片链接 24 小时后失效，请及时下载。
```

### 预期时间
- API 响应时间：45-60 秒（4K 分辨率需要更长时间）

---

## ✅ 测试用例 3: 文生图 - Base64 格式测试

### 目的
验证 Base64 输出格式是否正常工作

### 测试步骤

1. **在 Claude Desktop 中输入**：
```
生成一张简约风格的企业 Logo，以 Base64 格式返回
```

2. **预期行为**：
- Claude 调用 `generate_image` 工具
- 参数：`prompt="简约风格的企业 Logo，蓝色和白色配色"`, `model="doubao-seedream-4.5"`, `size="1024x1024"`, `response_format="b64_json"`, `count=1`
- 返回 Base64 编码的图片数据
- Claude 可以直接显示图片（无需下载）

3. **验证点**：
- ✅ Base64 格式正常工作
- ✅ 图片可以在 Claude 中直接预览
- ✅ 无需额外的下载步骤

### 预期输出示例

```
✅ 成功生成 1 张图片！

**模型**: doubao-seedream-4.5
**提示词**: 简约风格的企业 Logo，蓝色和白色配色
**尺寸**: 1024x1024
**格式**: Base64 (直接返回图片数据)

**图片**:
[Image content - Base64 data displayed]
```

### 预期时间
- API 响应时间：15-30 秒（Base64 格式与 URL 格式时间相近）

---

## ✅ 测试用例 4: 多张生成测试

### 目的
验证批量生成功能是否正常工作

### 测试步骤

1. **在 Claude Desktop 中输入**：
```
生成 3 张不同风格的城市夜景，使用 2K 分辨率
```

2. **预期行为**：
- Claude 调用 `generate_image` 工具
- 参数：`prompt="3 张不同风格的城市夜景，包括霓虹灯、高楼、赛博朋克风格"`, `model="doubao-seedream-4.5"`, `size="2K"`, `count=3`
- 生成 3 张 2K 分辨率的图片
- 每张图片风格不同

3. **验证点**：
- ✅ 成功生成 3 张图片
- ✅ 批量生成功能正常
- ✅ 返回 3 个不同的图片链接

### 预期输出示例

```
✅ 成功生成 3 张图片！

**模型**: doubao-seedream-4.5
**提示词**: 3 张不同风格的城市夜景，包括霓虹灯、高楼、赛博朋克风格
**尺寸**: 2K
**数量**: 3

**图片链接**:
1. 霓虹灯闪烁的城市夜景.jpg
2. 高楼林立的夜景.jpg
3. 赛博朋克风格的都市.jpg

⚠️ 注意：图片链接 24 小时后失效，请及时下载。
```

### 预期时间
- API 响应时间：60-120 秒（3 张图片需要更长时间）

---

## ✅ 测试用例 5: 图生图测试

### 目的
验证图生图功能是否正常工作

### 测试步骤

1. **先准备参考图**
   - 上传一张参考图片到网盘或其他可访问的地方
   - 获取图片 URL

2. **在 Claude Desktop 中输入**：
```
根据这张图片的风格，生成一张新的商务肖像
```

3. **Claude 会询问**：
   ```
   请提供参考图片的 URL（最多 14 张）
   ```

4. **提供 URL**：
   ```
   https://example.com/reference.jpg
   ```

5. **预期行为**：
- Claude 调用 `image_to_image` 工具
- 参数：`prompt="根据这张图片的风格，生成一张新的商务肖像，背景简洁专业"`, `image_urls=["https://example.com/reference.jpg"]`, `model="doubao-seedream-4.5"`, `size="2K"`
- 根据参考图生成新图片
- 保持原图的商务风格

6. **验证点**：
- ✅ 成功调用图生图功能
- ✅ 基于参考图生成新图片
- ✅ 返回新图片下载链接

### 预期输出示例

```
✅ 成功生成 1 张图片！

**模型**: doubao-seedream-4.5
**提示词**: 根据这张图片的风格，生成一张新的商务肖像，背景简洁专业
**参考图**: 1 张
**尺寸**: 2K

**图片链接**:
https://ark-cn-beijing.volces.com/images/generated_xxx.jpg

⚠️ 注意：图片链接 24 小时后失效，请及时下载。
```

### 预期时间
- API 响应时间：45-90 秒（图生图需要处理参考图）

---

## ✅ 测试用例 6: 组图生成测试

### 目的
验证组图生成功能是否正常工作

### 测试步骤

1. **在 Claude Desktop 中输入**：
```
生成一组 4 张科幻风格的太空探索主题插画，内容连贯
```

2. **预期行为**：
- Claude 调用 `generate_image_set` 工具
- 参数：`prompt="科幻风格的太空探索主题插画，展现从城市到太空的探索历程，内容连贯"`, `model="doubao-seedream-4.5"`, `count=4`, `size="2K"`
- 生成 4 张内容关联的科幻插画

3. **验证点**：
- ✅ 成功生成 4 张图片
- ✅ 组图生成功能正常
- ✅ 4 张图片内容连贯（太空主题）

### 预期输出示例

```
✅ 成功生成 4 张组图！

**模型**: doubao-seedream-4.5
**提示词**: 科幻风格的太空探索主题插画，展现从城市到太空的探索历程，内容连贯
**数量**: 4
**尺寸**: 2K

**图片链接**:
1. 太空探索-城市起点.jpg
2. 太空探索-进入轨道.jpg
3. 太空探索-月球基地.jpg
4. 太空探索-太空站.jpg

⚠️ 注意：图片链接 24 小时后失效，请及时下载。
```

### 预期时间
- API 响应时间：120-180 秒（4 张组图需要较长时间）

---

## ✅ 测试用例 7: 模型列表查询测试

### 目的
验证查询模型列表功能

### 测试步骤

1. **在 Claude Desktop 中输入**：
```
列出所有支持的模型和它们的功能
```

2. **预期行为**：
- Claude 调用 `list_models` 工具
- 返回所有支持的模型及其功能说明

3. **验证点**：
- ✅ 成功调用模型列表功能
- ✅ 显示所有 4 个模型的详细信息
- ✅ 每个模型的功能说明清晰

### 预期输出示例

```
📋 火山引擎豆包生图 - 支持的模型列表

- **doubao-seedream-4.5**: 豆包生图 4.5 (最新，支持多格式)
  支持功能：文生图、图生图、组图生成、多图生图
- **doubao-seedream-4.0**: 豆包生图 4.0
  支持功能：文生图、图生图、组图生成、多图生图
- **doubao-seedream-3.0-t2i**: 豆包生图 3.0 文生图
  支持功能：仅文生图
- **doubao-seedream-3.0-i2i**: 豆包生图 3.0 图生图
  支持功能：仅图生图

🎨 支持的尺寸：
- 2K, 4K, 1024x1024, 2048x2048

💡 提示：
- doubao-seedream-3.0-t2i 仅支持文生图
- doubao-seedream-3.0-i2i 仅支持图生图
- doubao-seedream-4.0/4.5 支持文生图、图生图、组图生成、多图生图
```

### 预期时间
- 即时返回（无需 API 调用）

---

## ✅ 测试用例 8: 错误处理测试

### 目的
验证错误处理是否正常工作

### 测试步骤

1. **测试未设置 API Key**：
   - 在环境变量中不设置 `ARK_API_KEY`
   - 在 Claude Desktop 中输入：```
生成一张测试图片
```

2. **预期行为**：
- Claude 调用 `generate_image` 工具
- 返回错误消息："❌ 错误：未设置 ARK_API_KEY 环境变量。请设置火山引擎 API Key。"
- 清晰的错误提示

3. **验证点**：
- ✅ 错误处理正常
- ✅ 提示用户如何设置 API Key

### 预期输出示例

```
❌ 错误：未设置 ARK_API_KEY 环境变量。请设置火山引擎 API Key。
```

### 测试步骤：测试无效模型

4. **在 Claude Desktop 中输入**：
```
使用模型 model-xyz-xyz 生成一张风景画
```

5. **预期行为**：
- Claude 调用 `generate_image` 工具
- 参数包含无效模型 ID
- 返回错误消息："❌ 错误：不支持的模型 "model-xyz-xyz"。支持的模型：..."
- 显示所有支持的模型列表

6. **验证点**：
- ✅ 错误处理正常
- ✅ 提供可用模型列表
- ✅ 帮助用户选择正确的模型

### 预期输出示例

```
❌ 错误：不支持的模型 "model-xyz-xyz"。支持的模型：

📋 火山引擎豆包生图 - 支持的模型列表

- **doubao-seedream-4.5**: 豆包生图 4.5 (最新，支持多格式)
  支持功能：文生图、图生图、组图生成、多图生图
- **doubao-seedream-4.0**: 豆包生图 4.0
  支持功能：文生图、图生图、组图生成、多图生图
...
```

---

## ⚠️ 测试注意事项

### 1. API Key 安全
- ⚠️ **不要**在公开场合分享 API Key
- ⚠️ **定期**更换 API Key 以保证安全
- ⚠️ **建议**为不同项目使用不同的 API Key

### 2. 成本控制
- 💰 4K 分辨率生成时间约为 2K 的 2-3 倍
- 💰 组图生成（15 张）可能需要 10-15 分钟
- 💰 建议：先用 2K 分辨率测试，确认功能正常后再使用高分辨率

### 3. 图片下载
- ⚠️ 图片链接 **24 小时后失效**
- 💰 重要图片建议使用 `response_format: "b64_json"` 直接获取数据
- 💰 如果使用 URL 格式，请及时下载保存

### 4. 性能参考

| 操作类型 | 预期时间 | 实际范围 |
|-----------|---------|-----------|
| 单张文生图 (2K) | 15-30 秒 | - |
| 单张文生图 (4K) | 45-90 秒 | - |
| 多张文生图 (3 张) | 60-120 秒 | - |
| 图生图 (1 张) | 45-90 秒 | - |
| 组图生成 (4 张) | 2-4 分钟 | - |
| 组图生成 (15 张) | 10-15 分钟 | - |

### 5. 提示词优化建议

#### 提高成功率

1. **详细描述**：包含主体、风格、光线、背景、颜色
   - ❌ "一只猫"
   - ✅ "一只毛茸茸的橘色小猫，坐在阳光下，毛发闪闪发光，眼神温暖好奇，背景是绿草地和蓝天，细节丰富，光影效果出色，专业摄影质量"

2. **指定风格**：明确指出想要的风格
   - ❌ "风景画"
   - ✅ "日式动漫风格的山水风景画，细腻线条，柔和色彩，治愈系风格"

3. **中英文混合**：模型对中英文都有良好理解
   - ✅ "专业摄影师拍摄的商业肖像，自然光，眼神自信，8K分辨率"
   - ✅ "Photorealistic portrait, natural lighting, confident eyes, 8K resolution"

4. **添加质量关键词**：
   - ✅ "高清"、"4K"、"专业摄影"
   - ✅ "high resolution", "professional photography quality", "4K resolution"

5. **调整文本权重**：
   - 自由创作：1.0-3.0
   - 平衡创作：2.5-5.0
   - 严格遵循：6.0-10.0

---

## 📊 测试结果记录模板

### 测试记录表

| 测试编号 | 测试名称 | 状态 | 结果描述 | 响应时间 | 备注 |
|---------|---------|------|----------|---------|------|
| TC001 | 基本文生图 - 简单测试 | | | | |
| TC002 | 文生图 - 完整参数测试 | | | | |
| TC003 | 文生图 - Base64 格式测试 | | | | |
| TC004 | 多张生成测试 | | | | |
| TC005 | 图生图测试 | | | | |
| TC006 | 组图生成测试 | | | | |
| TC007 | 模型列表查询测试 | | | | |
| TC008 | 错误处理测试 | | | | |

### 测试执行记录示例

```
测试日期: 2026-01-20
测试人: Your Name
测试环境:
- Claude Desktop
- API Key: 已设置
- 项目版本: 1.0.0

测试执行记录:

[TC001] 2026-01-20 14:30 - 通过
  工具: generate_image
  参数: {"prompt":"简单的风景画","model":"doubao-seedream-4.5","size":"2K","count":1}
  结果: ✅ 成功生成 1 张 2K 分辨率图片
  响应时间: 22 秒
  备注: 功能正常

[TC002] 2026-01-20 14:35 - 通过
  工具: generate_image
  参数: {"prompt":"专业摄影师拍摄的人像","model":"doubao-seedream-4.5","size":"4K","guidance_scale":7.5,"watermark":true,"count":1}
  结果: ✅ 成功生成 1 张 4K 分辨率图片
  响应时间: 68 秒
  备注: 水印功能正常，高质量输出

...
```

---

## 🎯 快速测试清单

执行所有测试用例前，确认以下项目：

### 功能测试

- [ ] TC001: 基本文生图 - 简单测试
- [ ] TC002: 文生图 - 完整参数测试
- [ ] TC003: 文生图 - Base64 格式测试
- [ ] TC004: 多张生成测试
- [ ] TC005: 图生图测试
- [ ] TC006: 组图生成测试
- [ ] TC007: 模型列表查询测试
- [ ] TC008: 错误处理测试

### 集成测试

- [ ] Claude Desktop 集成测试
- [ ] VS Code 集成测试
- [ ] Cursor 集成测试

### 边界情况测试

- [ ] API Key 未设置错误处理
- [ ] 无效模型 ID 错误处理
- [ ] 无效尺寸错误处理
- [ ] API 调用失败错误处理

---

## 📝 测试总结模板

```
测试总结报告
日期: 2026-01-20
测试人: Your Name
项目: 火山引擎 AI 生图 MCP 工具
版本: 1.0.0

测试统计:
- 总测试用例: 8 个
- 通过测试: 0 个
- 失败测试: 0 个
- 成功率: 0%

测试覆盖范围:
- ✅ 文生图功能: 已覆盖
- ✅ 图生图功能: 已覆盖
- ✅ 组图生成功能: 已覆盖
- ✅ 模型列表查询: 已覆盖
- ✅ 错误处理: 已覆盖

性能表现:
- 平均响应时间: 35 秒
- 最快响应: 15 秒
- 最慢响应: 120 秒
- 性能评级: 良好

问题与改进:
- 发现问题: 无
- 改进建议: 无

结论:
✅ 所有核心功能工作正常
✅ 错误处理完善
✅ 文档清晰完整
✅ 可以投入使用

建议:
- 项目可以发布使用
- 建议提供更多使用示例
- 建议添加自动化测试脚本
```

---

## 🔧 自动化测试脚本（可选）

如果需要自动化测试，可以创建以下脚本：

### Python 测试脚本示例

```python
import asyncio
import json

async def test_generate_image():
    """测试文生图功能"""
    test_prompt = "简单的风景画"
    
    # 模拟 MCP 调用
    print(f"测试文生图功能...")
    print(f"提示词: {test_prompt}")
    print(f"模型: doubao-seedream-4.5")
    print(f"尺寸: 2K")
    
    # 这里可以添加实际的 API 调用代码
    # await call_volcengine_api(...)
    
    print("✅ 测试完成")

async def main():
    await test_generate_image()

if __name__ == "__main__":
    asyncio.run(main())
```

### 测试报告生成

```bash
# 创建测试报告
cat > test_report.md << EOF
# 火山引擎 AI 生图 MCP 工具 - 测试报告
EOF

# 为每个测试用例添加测试结果
echo "[TC001] 测试通过" >> test_report.md
```

---

## 📞 后续步骤

1. ✅ 执行所有测试用例
2. 📝 记录测试结果
3. 📊 生成测试总结报告
4. 🎯 根据测试结果优化代码
5. 🚀 发布项目

---

## 💡 测试技巧

### 1. 渐进式测试
从简单的功能开始，逐步测试复杂功能
- 第一批：基本文生图（TC001）
- 第二批：完整参数测试（TC002-TC003）
- 第三批：高级功能测试（TC004-TC006）

### 2. 对比测试
使用相同的提示词测试不同的模型和参数，对比效果
- 有助于选择最佳的配置组合

### 3. 边界测试
测试系统在边界情况下的行为
- 测试最大/最小参数值
- 测试无效输入处理

### 4. 性能测试
记录每次 API 调用的响应时间
- 分析性能瓶颈
- 优化参数组合

### 5. 回归测试
重复关键测试用例，确保结果稳定可靠
- 避免随机性导致的偶发问题

---

## 📋 测试完成标志

当完成以下所有测试项目后，可以认为测试阶段完成：

- [ ] 所有基础功能测试通过
- [ ] 所有错误处理测试通过
- [ ] 所有高级功能测试通过
- [ ] 性能测试完成
- [ ] 测试报告生成
- [ ] 所有已知问题已记录
- [ ] 项目文档已更新

---

**建议**: 创建 GitHub Issues 跟踪测试进度和问题

---

## 🎉 祝你测试顺利！

如果你在测试过程中遇到任何问题，请：

1. 查看错误信息中的详细说明
2. 检查 API Key 是否正确配置
3. 验证网络连接是否正常
4. 查看本文档中的故障排查部分

---

**文档版本**: 1.0.0
**最后更新**: 2026-01-20
**维护者**: Volcengine ImageGen MCP Team


## 🚀 快速开始

### 1. 安装依赖

```bash
cd volcengine-imagegen-mcp
npm install
```

### 2. 配置 API Key

```bash
# Windows CMD
set ARK_API_KEY=你的API密钥

# PowerShell
$env:ARK_API_KEY="你的API密钥"

# Linux/macOS
export ARK_API_KEY="你的API密钥"
```

### 3. 构建项目

```bash
npm run build
```

### 4. 启动服务器

```bash
# 使用 Node.js 直接运行
node dist/index.js

# 或者使用 npm script
npm start

# 或者直接使用 npx（推荐，无需安装）
npx volcengine-imagegen-mcp
```

## 📋 使用示例

### 示例 1: 文生图 - 基本使用

**场景**: 生成一张简单的风景画

```
工具: generate_image
参数:
{
  "prompt": "一幅美丽的山水风景画，云雾缭绕，阳光穿透云层",
  "model": "doubao-seedream-4.5",
  "size": "2K",
  "count": 1
}
```

**预期结果**:
- 生成 1 张 2K 分辨率的山水风景画
- 返回图片下载链接

---

### 示例 2: 文生图 - 高质量输出

**场景**: 生成 4K 高清人物肖像

```
工具: generate_image
参数:
{
  "prompt": "专业摄影师拍摄的商业肖像，自然光，眼神自信，背景简洁，8K分辨率",
  "model": "doubao-seedream-4.5",
  "size": "4K",
  "guidance_scale": 7.5,
  "response_format": "url",
  "watermark": false
}
```

**预期结果**:
- 生成 1 张 4K 分辨率的专业肖像
- 高文本权重（7.5）严格遵循提示词
- 无水印

---

### 示例 3: 文生图 - 多图生成

**场景**: 生成 3 张不同风格的城市夜景

```
工具: generate_image
参数:
{
  "prompt": "赛博朋克风格的城市夜景，霓虹灯，高楼林立，雨后的街道反射",
  "model": "doubao-seedream-4.5",
  "size": "2048x2048",
  "count": 3,
  "guidance_scale": 5.0
}
```

**预期结果**:
- 生成 3 张 2048x2048 分辨率的赛博朋克城市夜景
- 中等文本权重（5.0）平衡创意和提示词

---

### 示例 4: 图生图

**场景**: 根据参考图生成相似风格的新图片

```
工具: image_to_image
参数:
{
  "prompt": "保持原图的构图和风格，但将光线调整为黄金时刻的暖色调",
  "model": "doubao-seedream-4.5",
  "image_urls": ["https://example.com/reference-image.jpg"],
  "size": "2K",
  "guidance_scale": 6.0
}
```

**预期结果**:
- 根据参考图生成新图片
- 调整光线为黄金时刻暖色调
- 保持原图构图和风格

---

### 示例 5: 组图生成

**场景**: 生成一组 4 张连续的科幻主题插画

```
工具: generate_image_set
参数:
{
  "prompt": "未来城市的空中花园，悬浮在云层之上，融合科技与自然元素",
  "model": "doubao-seedream-4.5",
  "count": 4,
  "size": "2K",
  "guidance_scale": 4.5,
  "response_format": "b64_json",
  "watermark": false
}
```

**预期结果**:
- 生成 4 张内容关联的科幻主题插画
- 以 Base64 格式直接返回图片数据
- 内容连续性强，可以组成系列

---

### 示例 6: 查询模型列表

**场景**: 了解支持的模型及其功能

```
工具: list_models
参数: {}
```

**预期结果**:
返回所有支持的模型列表及其说明。

---

### 示例 7: 图生图 - 多参考图

**场景**: 根据多张参考图生成新风格

```
工具: image_to_image
参数:
{
  "prompt": "融合以下图片的风格，创造全新的设计",
  "model": "doubao-seedream-4.5",
  "image_urls": [
    "https://example.com/ref1.jpg",
    "https://example.com/ref2.jpg",
    "https://example.com/ref3.jpg"
  ],
  "size": "2K"
}
```

**预期结果**:
- 综合多张参考图的风格
- 生成全新设计的图片

---

### 示例 8: 文生图 - Base64 输出

**场景**: 生成图片并直接获取 Base64 数据用于嵌入

```
工具: generate_image
参数:
{
  "prompt": "简约风格的企业 Logo 设计，蓝色和白色配色",
  "model": "doubao-seedream-4.5",
  "size": "1024x1024",
  "response_format": "b64_json",
  "watermark": false
}
```

**预期结果**:
- 以 Base64 JSON 格式返回图片
- 可以直接嵌入 HTML 或应用中
- 不需要额外的下载步骤

---

## 🎯 提示词优化技巧

### 中文提示词示例

#### 风格描述
- **写实风格**: "写实风格，细腻的光影效果，专业摄影质量"
- **动漫风格**: "日式动漫风格，精细线条，鲜艳色彩"
- **油画风格**: "印象派油画风格，厚涂笔触，丰富色彩层次"
- **赛博朋克**: "赛博朋克风格，霓虹灯效，未来科技感"

#### 场景描述
- **自然风景**: "雪山日出，云海翻涌，金色阳光穿透云层，壮丽自然风光"
- **城市建筑**: "现代都市天际线，玻璃幕墙建筑反射晚霞，繁华都市夜景"
- **人物肖像**: "特写人像，柔和自然光，眼神温暖自信，背景虚化突出主体"

#### 细节强化
- **光线描述**: "侧光打亮轮廓，体积光增加立体感，色彩饱和度适中"
- **构图指导**: "三分法构图，主体位于黄金分割点，背景简洁不抢眼"
- **色彩控制**: "冷暖色调对比，蓝色和橙色搭配，营造梦幻氛围"

### 英文提示词示例

#### Style Descriptions
- **Photorealistic**: "Photorealistic, detailed lighting, professional photography quality, 8K resolution"
- **Anime Style**: "Japanese anime style, clean lines, vibrant colors, expressive characters"
- **Oil Painting**: "Impressionist oil painting style, thick brushstrokes, rich color layers"
- **Cyberpunk**: "Cyberpunk aesthetic, neon lighting, futuristic technology elements"

#### Scene Descriptions
- **Natural Landscape**: "Mountain sunrise, sea of clouds, golden sunlight piercing through, magnificent natural scenery"
- **City Architecture**: "Modern city skyline, glass curtain buildings reflecting sunset, bustling urban night view"
- **Portrait**: "Close-up portrait, soft natural light, warm confident eyes, blurred background"

#### Detail Enhancement
- **Lighting**: "Side light contour, volumetric lighting for depth, balanced color saturation"
- **Composition**: "Rule of thirds, subject at golden ratio point, clean background"
- **Color**: "Cool-warm contrast, blue and orange palette, dreamlike atmosphere"

---

## 🔧 高级用法

### 组合多个参数

```
工具: generate_image
参数:
{
  "prompt": "超写实 3D 渲染的未来汽车，光滑金属表面，充满科技感的细节，8K质量",
  "model": "doubao-seedream-4.5",
  "size": "4K",
  "guidance_scale": 8.5,
  "response_format": "b64_json",
  "watermark": false,
  "count": 2
}
```

### 批量生成不同尺寸

```
任务 1: 生成 2K 尺寸
参数: { "prompt": "...", "size": "2K" }

任务 2: 生成 4K 尺寸
参数: { "prompt": "...", "size": "4K" }

任务 3: 生成 1024x1024 尺寸
参数: { "prompt": "...", "size": "1024x1024" }
```

---

## ⚙️ 故障排查

### 问题: "未设置 ARK_API_KEY 环境变量"

**解决方案**:
```bash
# 检查环境变量是否设置
echo $ARK_API_KEY  # Linux/macOS
echo %ARK_API_KEY%  # Windows CMD
echo $env:ARK_API_KEY  # PowerShell

# 如果未设置，请重新设置
export ARK_API_KEY="你的API密钥"
```

### 问题: "API 调用失败"

**可能原因**:
1. API Key 无效或已过期
2. 网络连接问题
3. API 服务暂时不可用

**解决方案**:
1. 检查 API Key 是否正确
2. 测试网络连接
3. 查看火山引擎控制台的状态页

### 问题: "生成的图片质量不佳"

**优化建议**:
1. 提示词更详细具体
2. 调整 `guidance_scale` 参数
3. 尝试不同的 `size` 设置
4. 参考"提示词优化技巧"章节

### 问题: "图片链接失效"

**说明**: 图片链接 24 小时后自动失效

**解决方案**:
- 及时下载图片
- 使用 `response_format: "b64_json"` 直接获取 Base64 数据

---

## 📊 性能参考

### 生成时间参考（单张图片）

| 分辨率 | 平均时间 | 说明 |
|--------|---------|------|
| 1024x1024 | 15-30秒 | 适合快速测试 |
| 2K | 30-60秒 | 平衡质量和速度 |
| 4K | 60-120秒 | 最高质量，需要更多时间 |

### 组图生成时间参考

| 图片数量 | 平均时间 | 说明 |
|---------|---------|------|
| 4 张 | 2-4分钟 | 快速生成 |
| 8 张 | 5-8分钟 | 中等批量 |
| 15 张 | 10-15分钟 | 最大批量 |

**注意**: 实际时间可能因网络、服务器负载等因素有所差异。

---

## 🎨 创意工作流

### 工作流 1: 生成多版本选优

```
1. 使用 generate_image，相同提示词，guidance_scale 从 3.0 到 8.0，步长 0.5
2. 对比生成的图片，选择最佳版本
3. 基于最佳版本，调整提示词再次生成
```

### 工作流 2: 风格迁移

```
1. 使用 image_to_image，上传参考图
2. 提示词描述目标风格（如"改为油画风格"）
3. 生成新图片，检查风格迁移效果
4. 如效果不理想，调整提示词重试
```

### 工作流 3: 系列插画生成

```
1. 使用 generate_image_set，count 设为 4-6
2. 编写连贯的提示词（如"第一章：..."）
3. 生成系列图片
4. 使用 image_to_image 基于前面生成的图，微调后续图片
```

---

## 📚 更多资源

- [火山引擎官方文档](https://www.volcengine.com/docs/82379/)
- [火山方舟控制台](https://console.volcengine.com/ark/)
- [MCP 协议规范](https://modelcontextprotocol.io/)
- [火山引擎 MCP 市场](https://www.volcengine.com/mcp-marketplace)
