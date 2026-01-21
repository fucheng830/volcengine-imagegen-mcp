#!/usr/bin/env node
/**
 * 火山引擎 AI 生图 MCP 服务器
 * 纯 Node.js + TypeScript 实现（不使用 zod）
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import axios from "axios";

// 配置和常量
const API_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3";
const API_KEY = process.env.ARK_API_KEY;

if (!API_KEY) {
  console.error("错误：未设置 ARK_API_KEY 环境变量");
  console.error("请设置火山引擎 API Key");
  process.exit(1);
}

const SUPPORTED_MODELS: Record<string, string> = {
  "doubao-seedream-4-5-251128": "豆包生图 4.5 (最新，支持多格式)",
  "doubao-seedream-4-0-250828": "豆包生图 4.0",
  "doubao-seedream-3-0-t2i-250415": "豆包生图 3.0 文生图",
  "doubao-seedream-3-0-i2i": "豆包生图 3.0 图生图",
};

const SUPPORTED_SIZES = ["2K", "4K", "1024x1024", "2048x2048"];

// API 调用函数
async function generateSingleImage(params: any): Promise<any> {
  try {
    const response = await axios.post(
      `${API_BASE_URL}/images/generations`,
      {
        model: params.model || "doubao-seedream-4-5-251128",
        prompt: params.prompt,
        size: params.size || "2K",
        guidance_scale: params.guidance_scale || 2.5,
        watermark: params.watermark || false,
        response_format: params.response_format || "url",
      },
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${API_KEY}`,
        },
        timeout: 120000,
      }
    );

    return response.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      const errorData = error.response?.data;
      const errorMessage = errorData?.error?.message || error.message;
      throw new Error(`API 调用失败：${errorMessage}`);
    }
    throw error;
  }
}

// 工具定义
const tools = [
  {
    name: "generate_image",
    description: "生成图片（文生图）。使用文字描述生成一张图片。",
    inputSchema: {
      type: "object",
      properties: {
        model: {
          type: "string",
          description: "使用的模型ID",
          default: "doubao-seedream-4-5-251128",
        },
        prompt: {
          type: "string",
          description: "图片生成提示词（支持中英文）",
          minLength: 1,
          maxLength: 2000,
        },
        size: {
          type: "string",
          description: "图片尺寸",
          enum: SUPPORTED_SIZES,
          default: "2K",
        },
        guidance_scale: {
          type: "number",
          description: "文本权重（1-10）",
          minimum: 1,
          maximum: 10,
          default: 2.5,
        },
        watermark: {
          type: "boolean",
          description: "是否添加水印",
          default: false,
        },
        count: {
          type: "number",
          description: "生成图片数量（当前仅支持1张）",
          minimum: 1,
          maximum: 1,
          default: 1,
        },
        response_format: {
          type: "string",
          description: "响应格式：url 或 b64_json",
          enum: ["url", "b64_json"],
          default: "url",
        },
      },
      required: ["prompt"],
    },
  },
  {
    name: "image_to_image",
    description: "图生图。基于参考图片生成新图片。",
    inputSchema: {
      type: "object",
      properties: {
        model: {
          type: "string",
          description: "使用的模型ID（仅支持 4.5/4.0）",
          default: "doubao-seedream-4-5-251128",
        },
        prompt: {
          type: "string",
          description: "图片生成提示词",
          minLength: 1,
          maxLength: 2000,
        },
        image_urls: {
          type: "array",
          description: "参考图片 URL 列表（最多14张）",
          items: {
            type: "string",
            format: "uri",
          },
          minItems: 1,
          maxItems: 14,
        },
        size: {
          type: "string",
          description: "图片尺寸",
          enum: SUPPORTED_SIZES,
          default: "2K",
        },
        guidance_scale: {
          type: "number",
          description: "文本权重",
          minimum: 1,
          maximum: 10,
          default: 2.5,
        },
        response_format: {
          type: "string",
          description: "响应格式",
          enum: ["url", "b64_json"],
          default: "url",
        },
      },
      required: ["prompt", "image_urls"],
    },
  },
  {
    name: "generate_image_set",
    description: "批量生成图片。生成多张内容相关的图片（通过多次调用实现）。",
    inputSchema: {
      type: "object",
      properties: {
        model: {
          type: "string",
          description: "使用的模型ID",
          default: "doubao-seedream-4-5-251128",
        },
        prompt: {
          type: "string",
          description: "图片生成提示词",
          minLength: 1,
          maxLength: 2000,
        },
        count: {
          type: "number",
          description: "生成图片数量（2-15张）",
          minimum: 1,
          maximum: 15,
          default: 4,
        },
        size: {
          type: "string",
          description: "图片尺寸",
          enum: SUPPORTED_SIZES,
          default: "2K",
        },
        guidance_scale: {
          type: "number",
          description: "文本权重",
          minimum: 1,
          maximum: 10,
          default: 2.5,
        },
        response_format: {
          type: "string",
          description: "响应格式",
          enum: ["url", "b64_json"],
          default: "url",
        },
      },
      required: ["prompt", "count"],
    },
  },
  {
    name: "list_models",
    description: "获取支持的模型列表和功能说明",
    inputSchema: {
      type: "object",
      properties: {},
    },
  },
];

// 服务器设置
async function main() {
  console.log("✅ 火山引擎 AI 生图 MCP 服务器已启动！");
  console.log("📋 可用工具：");
  console.log("  - generate_image: 文生图");
  console.log("  - image_to_image: 图生图");
  console.log("  - generate_image_set: 批量生成");
  console.log("  - list_models: 获取模型列表");
  console.log("");

  const server = new Server(
    {
      name: "volcengine-imagegen-mcp",
      version: "1.0.0",
    },
    {
      capabilities: {
        tools: {},
      },
    }
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => {
    return {
      tools: tools,
    };
  });

  server.setRequestHandler(CallToolRequestSchema, async (request: any) => {
    const { name, arguments: args } = request.params;

    try {
      switch (name) {
        case "generate_image": {
          const response = await generateSingleImage(args);
          const images = response.data;
          const count = images.length;

          if (args.response_format === "b64_json") {
            return {
              content: [
                {
                  type: "image",
                  data: images[0].b64_json || "",
                  mimeType: "image/png",
                },
              ],
            };
          } else {
            const imageList = images
              .map((img: any, idx: number) => `${idx + 1}. ${img.url}`)
              .join("\n");

            return {
              content: [
                {
                  type: "text",
                  text: `✅ 成功生成 ${count} 张图片！

**模型**: ${response.model}
**提示词**: ${args.prompt}
**尺寸**: ${args.size}
**文本权重**: ${args.guidance_scale}
**水印**: ${args.watermark ? "是" : "否"}

**图片链接**:
${imageList}

⚠️ 注意：图片链接 24 小时后失效。`,
                },
              ],
            };
          }
        }

        case "image_to_image": {
          const response = await generateSingleImage(args);
          const images = response.data;

          if (args.response_format === "b64_json") {
            return {
              content: [
                {
                  type: "image",
                  data: images[0].b64_json || "",
                  mimeType: "image/png",
                },
              ],
            };
          } else {
            const imageList = images
              .map((img: any, idx: number) => `${idx + 1}. ${img.url}`)
              .join("\n");

            return {
              content: [
                {
                  type: "text",
                  text: `✅ 成功生成 ${images.length} 张图片！

**模型**: ${response.model}
**提示词**: ${args.prompt}
**参考图片**: ${args.image_urls.length} 张
**尺寸**: ${args.size}

**图片链接**:
${imageList}`,
                },
              ],
            };
          }
        }

        case "generate_image_set": {
          const count = Math.min(args.count, 15);
          const size = args.size;
          const response_format = args.response_format || "url";
          const images: any[] = [];

          for (let i = 0; i < count; i++) {
            const response = await generateSingleImage({
              model: args.model,
              prompt: args.prompt,
              size: size,
              guidance_scale: args.guidance_scale,
              response_format: response_format,
            });

            images.push(...response.data);
          }

          if (response_format === "b64_json") {
            return {
              content: [
                {
                  type: "image",
                  data: images[0].b64_json || "",
                  mimeType: "image/png",
                },
              ],
            };
          } else {
            const imageList = images
              .map((img: any, idx: number) => `${idx + 1}. ${img.url}`)
              .join("\n");

            return {
              content: [
                {
                  type: "text",
                  text: `✅ 成功生成 ${images.length} 张图片！

**模型**: ${args.model}
**提示词**: ${args.prompt}
**数量**: ${images.length} 张
**尺寸**: ${args.size}
**文本权重**: ${args.guidance_scale}

**图片链接**:
${imageList}

⚠️ 注意：图片链接 24 小时后失效。
💡 提示：当前通过 ${images.length} 次调用实现批量生成。`,
                },
              ],
            };
          }
        }

        case "list_models": {
          const modelsList = Object.entries(SUPPORTED_MODELS as Record<string, string>)
            .map(([k, v]) => `- **${k}**\n  ${v}`)
            .join("\n");

          const sizesList = SUPPORTED_SIZES.map((s) => `- ${s}`).join("\n");

          return {
            content: [
              {
                type: "text",
                text: `📋 火山引擎豆包生图 - 支持的模型列表

${modelsList}

🎨 支持的尺寸：
${sizesList}

💡 提示：
- doubao-seedream-3.0-t2i 仅支持文生图
- doubao-seedream-3.0-i2i 仅支持图生图
- doubao-seedream-4.0/4.5 支持文生图、图生图、组图生成

📊 注意事项：
- 批量生成功能通过多次调用 API 实现
- count 参数当前仅支持 1 张`,
              },
            ],
          };
        }

        default: {
          throw new Error(`Unknown tool: ${name}`);
        }
      }
    } catch (error: any) {
      return {
        content: [
          {
            type: "text",
            text: `❌ 错误：${(error as Error).message}`,
          },
        ],
        isError: true,
      };
    }
  });

  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((error) => {
  console.error("❌ 服务器启动失败：", error);
  process.exit(1);
});
