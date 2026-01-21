"""
测试火山引擎 API - 获取模型列表
"""

import httpx
import asyncio

API_KEY = "14bb7c84-411b-4729-9d45-d0ddaba61c41"

async def test_models_endpoint():
    """测试获取模型列表的端点"""
    
    # 可能的端点
    endpoints = [
        "https://ark.cn-beijing.volces.com/api/v3/models",
        "https://ark.cn-beijing.volces.com/api/v3/image/models",
        "https://ark.cn-beijing.volces.com/api/v3/chat/models",
        "https://ark.cn-beijing.volces.com/api/v3/ark/models",
    ]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("🔍 正在测试模型列表端点...\n")
    
    for url in endpoints:
        print(f"测试端点: {url}")
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url, headers=headers)
                print(f"  状态码: {response.status_code}")
                
                if response.status_code == 200:
                    print(f"  ✅ 找到有效端点！")
                    print(f"  响应: {response.text[:500]}...")
                    return url
                else:
                    print(f"  错误: {response.text[:200]}")
            
        except Exception as e:
            print(f"  异常: {str(e)[:100]}")
        
        print("-" * 60)
    
    print("\n⚠️ 未找到有效的模型列表端点")
    
    # 尝试不同的认证方式
    print("\n🔍 尝试不同的认证方式...")
    auth_methods = [
        {"Authorization": f"Bearer {API_KEY}"},
        {"X-API-Key": API_KEY},
        {"api-key": API_KEY},
    ]
    
    test_url = "https://ark.cn-beijing.volces.com/api/v3/models"
    for auth_header in auth_methods:
        print(f"\n测试认证: {list(auth_header.keys())[0]}")
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                headers = {
                    "Content-Type": "application/json",
                    **auth_header
                }
                response = await client.get(test_url, headers=headers)
                print(f"  状态码: {response.status_code}")
                if response.status_code == 200:
                    print(f"  ✅ 认证成功！")
                    print(f"  响应: {response.text[:500]}...")
                    return test_url
        except Exception as e:
            print(f"  异常: {str(e)[:100]}")

if __name__ == "__main__":
    asyncio.run(test_models_endpoint())
