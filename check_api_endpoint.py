"""
测试火山引擎 API 端点
"""

import httpx
import asyncio

API_KEY = "14bb7c84-411b-4729-9d45-d0ddaba61c41"

async def test_endpoints():
    """测试不同的 API 端点"""
    
    # 可能的端点组合
    base_urls = [
        "https://ark.cn-beijing.volces.com/api/v3",
        "https://ark.cn-beijing.volces.com/api/v3/images",
    ]
    
    endpoints = [
        "/generations",
        "/gen",
        "/create",
    ]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("🔍 正在测试火山引擎 API 端点...\n")
    
    for base_url in base_urls:
        for endpoint in endpoints:
            url = f"{base_url}{endpoint}"
            print(f"测试端点: {url}")
            
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    # 先测试 GET 请求
                    response = await client.get(url, headers=headers)
                    print(f"  GET 状态码: {response.status_code}")
                    
                    # 测试 POST 请求
                    test_payload = {
                        "model": "doubao-seedream-4.5",
                        "prompt": "test",
                    }
                    response = await client.post(url, headers=headers, json=test_payload)
                    print(f"  POST 状态码: {response.status_code}")
                    
                    if response.status_code != 404:
                        print(f"  ✅ 找到有效端点！")
                        print(f"  响应: {response.text[:300]}...")
                        return url
                    
            except Exception as e:
                print(f"  异常: {str(e)[:100]}")
            
            print("-" * 60)
    
    print("\n⚠️ 未找到有效的 API 端点")
    print("请检查火山引擎 API 文档确认正确的端点地址")

if __name__ == "__main__":
    asyncio.run(test_endpoints())
