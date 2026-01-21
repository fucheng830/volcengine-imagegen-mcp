"""
火山引擎 AI 生图 MCP 服务器
基于 Python 和 npx 的 Model Context Protocol (MCP) 服务器
"""

import os
import json
import asyncio
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool, TextContent, ImageContent
import httpx
from pydantic import BaseModel, Field


# ==================== 配置和常量 ====================

API_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

SUPPORTED_MODELS = {
    "doubao-seedream-4-5-251128": "豆包生图 4.5 (最新，支持多格式)",
    "doubao-seedream-4-0-250828": "豆包生图 4.0",
    "doubao-seedream-3-0-t2i-250415": "豆包生图 3.0 文生图",
    "doubao-seedream-3-0-i2i": "豆包生图 3.0 图生图 (模型ID未在列表中)"
}

SUPPORTED_SIZES = ["2K", "4K", "1024x1024", "2048x2048"]


# ==================== Pydantic 模型 ====================

class GenerateImageParams(BaseModel):
    """文生图参数"""
    model: str = Field(
        default="doubao-seedream-4-5-251128",
        description="使用的模型ID"
    )
    prompt: str = Field(
        ...,
        description="图片生成提示词（支持中英文，建议详细描述）",
        min_length=1,
        max_length=2000
    )
    size: str = Field(
        default="2K",
        description="图片尺寸：2K, 4K, 1024x1024, 2048x2048"
    )
    guidance_scale: float = Field(
        default=2.5,
        ge=1.0,
        le=10.0,
        description="文本权重（1-10），数值越大越严格遵循提示词"
    )
    response_format: str = Field(
        default="url",
        description="返回格式：url（下载链接）或 b64_json（Base64编码）"
    )
    watermark: bool = Field(
        default=False,
        description="是否添加水印"
    )
    count: int = Field(
        default=1,
        ge=1,
        le=1,
        description="生成图片数量（当前仅支持1张，批量生成功能暂不可用）"
    )


class ImageToImageParams(BaseModel):
    """图生图参数"""
    model: str = Field(
        default="doubao-seedream-4-5-251128",
        description="使用的模型ID（仅支持 doubao-seedream-4.5/4.0）"
    )
    prompt: str = Field(
        ...,
        description="图片生成提示词（支持中英文）",
        min_length=1,
        max_length=2000
    )
    image_urls: List[str] = Field(
        ...,
        description="参考图片 URL 列表（最多14张）",
        min_length=1,
        max_length=14
    )
    size: str = Field(
        default="2K",
        description="图片尺寸"
    )
    guidance_scale: float = Field(
        default=2.5,
        ge=1.0,
        le=10.0,
        description="文本权重（1-10）"
    )
    response_format: str = Field(
        default="url",
        description="返回格式"
    )
    watermark: bool = Field(
        default=False,
        description="是否添加水印"
    )


class GenerateImageSetParams(BaseModel):
    """组图生成参数"""
    model: str = Field(
        default="doubao-seedream-4-5-251128",
        description="使用的模型ID（仅支持 doubao-seedream-4.5/4.0）"
    )
    prompt: str = Field(
        ...,
        description="图片生成提示词",
        min_length=1,
        max_length=2000
    )
    count: int = Field(
        default=4,
        ge=2,
        le=15,
        description="生成图片数量（2-15张）"
    )
    size: str = Field(
        default="2K",
        description="图片尺寸"
    )
    guidance_scale: float = Field(
        default=2.5,
        ge=1.0,
        le=10.0,
        description="文本权重（1-10）"
    )
    response_format: str = Field(
        default="url",
        description="返回格式"
    )
    watermark: bool = Field(
        default=False,
        description="是否添加水印"
    )


# ==================== MCP 服务器初始化 ====================

mcp = FastMCP("volcengine-imagegen-mcp")


# ==================== 工具实现 ====================

@mcp.tool()
async def generate_image(
    model: str = "doubao-seedream-4.5",
    prompt: str = "",
    size: str = "2K",
    guidance_scale: float = 2.5,
    response_format: str = "url",
    watermark: bool = False,
    count: int = 1
) -> List[TextContent]:
    """文生图：根据文本提示词生成图片"""
    api_key = os.getenv("ARK_API_KEY")
    if not api_key:
        return [TextContent(
            type="text",
            text="❌ 错误：未设置 ARK_API_KEY 环境变量。请设置火山引擎 API Key。"
        )]
    
    # 验证模型
    if model not in SUPPORTED_MODELS:
        models_list = "\n".join([f"- {k}: {v}" for k, v in SUPPORTED_MODELS.items()])
        return [TextContent(
            type="text",
            text=f"❌ 错误：不支持的模型 \"{model}\"。支持的模型：\n{models_list}"
        )]
    
    # 验证尺寸
    if size not in SUPPORTED_SIZES:
        return [TextContent(
            type="text",
            text=f"❌ 错误：不支持的尺寸 \"{size}\"。支持的尺寸：{', '.join(SUPPORTED_SIZES)}"
        )]
    
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        payload = {
            "model": model,
            "prompt": prompt,
            "size": size,
            "guidance_scale": guidance_scale,
            "response_format": response_format,
            "watermark": watermark,
            "count": count
        }
        
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{API_BASE_URL}/images/generations",
                headers=headers,
                json=payload
            )
            
            response.raise_for_status()
            images = response.json().get("data", [])
            
            if response_format == "b64_json":
                # Base64 格式返回
                return [
                    ImageContent(
                        type="image",
                        data=img.get("b64_json", ""),
                        mimeType="image/png"
                    )
                    for img in images
                ]
            else:
                # URL 格式返回
                image_list = "\n".join([f"{idx+1}. {img.get('url', '')}" for idx, img in enumerate(images)])
                return [TextContent(
                    type="text",
                    text=f"""✅ 成功生成 {len(images)} 张图片！

**模型**: {model}
**提示词**: {prompt}
**尺寸**: {size}
**文本权重**: {guidance_scale}

**图片链接**:
{image_list}

⚠️ 注意：图片链接 24 小时后失效，请及时下载。"""
                )]
    
    except httpx.HTTPStatusError as e:
        error_msg = ""
        if hasattr(e.response, "json"):
            error_data = e.response.json()
            error_msg = error_data.get("error", {}).get("message", str(e))
        else:
            error_msg = str(e)
        
        return [TextContent(
            type="text",
            text=f"❌ API 调用失败：{error_msg}"
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"❌ 未知错误：{str(e)}"
        )]


@mcp.tool()
async def image_to_image(
    model: str = "doubao-seedream-4.5",
    prompt: str = "",
    image_urls: List[str] = [],
    size: str = "2K",
    guidance_scale: float = 2.5,
    response_format: str = "url",
    watermark: bool = False
) -> List[TextContent]:
    """图生图：根据参考图片和文本生成新图片"""
    api_key = os.getenv("ARK_API_KEY")
    if not api_key:
        return [TextContent(
            type="text",
            text="❌ 错误：未设置 ARK_API_KEY 环境变量。"
        )]
    
    # 验证模型是否支持图生图
    if not model.startswith("doubao-seedream-4"):
        return [TextContent(
            type="text",
            text=f"❌ 错误：图生图功能仅支持 doubao-seedream-4.5 和 4.0，当前模型：{model}"
        )]
    
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        payload = {
            "model": model,
            "prompt": prompt,
            "image_urls": image_urls,
            "size": size,
            "guidance_scale": guidance_scale,
            "response_format": response_format,
            "watermark": watermark
        }
        
        async with httpx.AsyncClient(timeout=180.0) as client:
            response = await client.post(
                f"{API_BASE_URL}/images/generations",
                headers=headers,
                json=payload
            )
            
            response.raise_for_status()
            images = response.json().get("data", [])
            
            if response_format == "b64_json":
                return [
                    ImageContent(
                        type="image",
                        data=img.get("b64_json", ""),
                        mimeType="image/png"
                    )
                    for img in images
                ]
            else:
                image_list = "\n".join([f"{idx+1}. {img.get('url', '')}" for idx, img in enumerate(images)])
                return [TextContent(
                    type="text",
                    text=f"""✅ 成功生成 {len(images)} 张图片！

**模型**: {model}
**提示词**: {prompt}
**参考图**: {len(image_urls)} 张
**尺寸**: {size}

**图片链接**:
{image_list}

⚠️ 注意：图片链接 24 小时后失效。"""
                )]
    
    except httpx.HTTPStatusError as e:
        error_msg = ""
        if hasattr(e.response, "json"):
            error_data = e.response.json()
            error_msg = error_data.get("error", {}).get("message", str(e))
        else:
            error_msg = str(e)
        
        return [TextContent(
            type="text",
            text=f"❌ API 调用失败：{error_msg}"
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"❌ 未知错误：{str(e)}"
        )]


@mcp.tool()
async def generate_image_set(
    model: str = "doubao-seedream-4.5",
    prompt: str = "",
    count: int = 4,
    size: str = "2K",
    guidance_scale: float = 2.5,
    response_format: str = "url",
    watermark: bool = False
) -> List[TextContent]:
    """组图生成：生成一组内容关联的图片（最多15张）"""
    api_key = os.getenv("ARK_API_KEY")
    if not api_key:
        return [TextContent(
            type="text",
            text="❌ 错误：未设置 ARK_API_KEY 环境变量。"
        )]
    
    # 验证模型
    if not model.startswith("doubao-seedream-4"):
        return [TextContent(
            type="text",
            text=f"❌ 错误：组图功能仅支持 doubao-seedream-4.5 和 4.0，当前模型：{model}"
        )]
    
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        payload = {
            "model": model,
            "prompt": prompt,
            "sequential_image_generation": "auto",  # 启用组图功能
            "count": count,
            "size": size,
            "guidance_scale": guidance_scale,
            "response_format": response_format,
            "watermark": watermark
        }
        
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{API_BASE_URL}/images/generations",
                headers=headers,
                json=payload
            )
            
            response.raise_for_status()
            images = response.json().get("data", [])
            
            if response_format == "b64_json":
                return [
                    ImageContent(
                        type="image",
                        data=img.get("b64_json", ""),
                        mimeType="image/png"
                    )
                    for img in images
                ]
            else:
                image_list = "\n".join([f"{idx+1}. {img.get('url', '')}" for idx, img in enumerate(images)])
                return [TextContent(
                    type="text",
                    text=f"""✅ 成功生成 {len(images)} 张组图！

**模型**: {model}
**提示词**: {prompt}
**数量**: {count}
**尺寸**: {size}

**图片链接**:
{image_list}

⚠️ 注意：图片链接 24 小时后失效。"""
                )]
    
    except httpx.HTTPStatusError as e:
        error_msg = ""
        if hasattr(e.response, "json"):
            error_data = e.response.json()
            error_msg = error_data.get("error", {}).get("message", str(e))
        else:
            error_msg = str(e)
        
        return [TextContent(
            type="text",
            text=f"❌ API 调用失败：{error_msg}"
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"❌ 未知错误：{str(e)}"
        )]


@mcp.tool()
async def list_models() -> List[TextContent]:
    """获取支持的模型列表"""
    models_list = "\n".join([f"- **{k}**\n  {v}" for k, v in SUPPORTED_MODELS.items()])
    sizes_list = "\n".join([f"- {s}" for s in SUPPORTED_SIZES])
    
    return [TextContent(
        type="text",
        text=f"""📋 火山引擎豆包生图 - 支持的模型列表

{models_list}

🎨 支持的尺寸：
{sizes_list}

💡 提示：
- doubao-seedream-3.0-t2i 仅支持文生图
- doubao-seedream-3.0-i2i 仅支持图生图
- doubao-seedream-4.0/4.5 支持文生图、图生图、组图生成"""
    )]


# ==================== 主程序 ====================

def main():
    """启动 MCP 服务器"""
    print("✅ 火山引擎 AI 生图 MCP 服务器已启动！")
    print("📋 可用工具：")
    print("  - generate_image: 文生图")
    print("  - image_to_image: 图生图")
    print("  - generate_image_set: 组图生成")
    print("  - list_models: 获取模型列表")
    
    # FastMCP 自动处理 asyncio
    mcp.run()


if __name__ == "__main__":
    main()
