"""
使用正确的模型 ID 测试火山引擎 API
"""

import httpx
import asyncio
import json

API_KEY = "14bb7c84-411b-4729-9d45-d0ddaba61c41"
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

# 正确的生图模型 ID
IMAGE_MODELS = {
    "doubao-seedream-4-5-251128": "豆包生图 4.5 (最新)",
    "doubao-seedream-4-0-250828": "豆包生图 4.0",
    "doubao-seedream-3-0-t2i-250415": "豆包生图 3.0 文生图"
}

async def test_image_generation_endpoint():
    """测试图片生成端点"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("🔍 正在测试不同的图片生成端点...\n")
    
    # 可能的端点
    endpoints = [
        "/images/generations",
        "/image/generations",
        "/images/generate",
        "/image/generate",
        "/image/create",
        "/images/create",
    ]
    
    for endpoint in endpoints:
        url = f"{BASE_URL}{endpoint}"
        print(f"测试端点: {url}")
        
        # 使用最新的模型进行测试
        model_id = "doubao-seedream-4-5-251128"
        
        payload = {
            "model": model_id,
            "prompt": "生成一张简单的风景画",
        }
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, headers=headers, json=payload)
                print(f"  状态码: {response.status_code}")
                
                if response.status_code != 404:
                    print(f"  ✅ 端点有效！")
                    print(f"  响应: {response.text[:500]}...")
                    
                    if response.status_code == 200:
                        return url
                else:
                    print(f"  错误: {response.text[:200]}")
        
        except Exception as e:
            print(f"  异常: {str(e)[:100]}")
        
        print("-" * 60)
    
    print("\n⚠️ 未找到有效的图片生成端点")
    return None


async def test_chat_endpoint():
    """测试对话端点（参考）"""
    
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("\n🔍 测试对话端点作为参考...")
    
    payload = {
        "model": "doubao-seed-1-6-251015",
        "messages": [
            {"role": "user", "content": "Hello"}
        ]
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(url, headers=headers, json=payload)
            print(f"状态码: {response.status_code}")
            
            if response.status_code == 200:
                print(f"✅ 对话端点工作正常")
                data = response.json()
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                print(f"响应: {content[:100]}...")
            
    except Exception as e:
        print(f"异常: {str(e)}")


async def main():
    """主函数"""
    print("🚀 开始测试火山引擎图片生成 API\n")
    print("="*60)
    
    # 测试图片生成端点
    image_endpoint = await test_image_generation_endpoint()
    
    # 测试对话端点作为参考
    await test_chat_endpoint()
    
    print("\n" + "="*60)
    
    if image_endpoint:
        print(f"\n✅ 找到有效的图片生成端点: {image_endpoint}")
        print("可以开始使用该端点进行图片生成了！")
    else:
        print("\n⚠️ 未找到有效的图片生成端点")
        print("可能的原因：")
        print("1. 图片生成功能在不同的端点")
        print("2. 需要特殊的权限或认证方式")
        print("3. 图片生成 API 可能与对话 API 分离")
        print("\n建议：")
        print("- 查看火山引擎控制台的 API 文档")
        print("- 联系火山引擎技术支持")
        print("- 确认当前 API Key 是否包含图片生成权限")


if __name__ == "__main__":
    asyncio.run(main())
