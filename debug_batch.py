"""
调试批量生成功能，查看 API 实际响应
"""

import httpx
import asyncio
import json

API_KEY = "14bb7c84-411b-4729-9d45-d0ddaba61c41"
API_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

async def debug_batch_generation():
    """调试批量生成功能"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("🔍 调试批量生成功能...\n")
    
    # 测试不同的 count 参数值
    test_cases = [
        {
            "name": "count=1 (单张)",
            "payload": {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成一张城市夜景",
                "size": "2K",
                "count": 1
            }
        },
        {
            "name": "count=2 (两张)",
            "payload": {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成两张城市夜景",
                "size": "2K",
                "count": 2
            }
        },
        {
            "name": "count=3 (三张)",
            "payload": {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成三张城市夜景",
                "size": "2K",
                "count": 3
            }
        },
        {
            "name": "count=4 (四张)",
            "payload": {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成四张城市夜景",
                "size": "2K",
                "count": 4
            }
        },
        {
            "name": "n=3 (使用 n 参数)",
            "payload": {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成三张城市夜景",
                "size": "2K",
                "n": 3
            }
        },
        {
            "name": "num_images=3 (使用 num_images 参数)",
            "payload": {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成三张城市夜景",
                "size": "2K",
                "num_images": 3
            }
        }
    ]
    
    for test_case in test_cases:
        print(f"\n{'='*80}")
        print(f"测试: {test_case['name']}")
        print(f"{'='*80}")
        
        print(f"请求参数:")
        print(f"  {json.dumps(test_case['payload'], indent=4, ensure_ascii=False)}")
        
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{API_BASE_URL}/images/generations",
                    headers=headers,
                    json=test_case['payload']
                )
                
                print(f"\n响应状态码: {response.status_code}")
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"\n响应数据:")
                    print(f"  model: {data.get('model')}")
                    print(f"  created: {data.get('created')}")
                    print(f"  data 数量: {len(data.get('data', []))}")
                    
                    if data.get('data'):
                        for idx, img in enumerate(data['data']):
                            print(f"  图片 {idx+1}:")
                            print(f"    URL: {img.get('url', 'N/A')[:100]}...")
                            if 'b64_json' in img:
                                print(f"    Base64 长度: {len(img.get('b64_json', ''))}")
                    
                    print(f"\n✅ 成功！")
                else:
                    print(f"\n❌ 失败")
                    print(f"错误: {response.text}")
        
        except Exception as e:
            print(f"\n❌ 异常: {str(e)}")
    
    print(f"\n{'='*80}")
    print("🔍 结论:")
    print(f"{'='*80}")
    print("\n根据测试结果，判断哪个参数有效：")
    print("- 如果所有 count 值都只返回 1 张，说明 API 不支持批量生成")
    print("- 如果 n 或 num_images 参数有效，需要使用这些参数")
    print("- 如果某个参数值有效，需要限制在特定范围内")

if __name__ == "__main__":
    asyncio.run(debug_batch_generation())
