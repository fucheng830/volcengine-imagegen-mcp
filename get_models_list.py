"""
获取完整的火山引擎模型列表
"""

import httpx
import asyncio
import json

API_KEY = "14bb7c84-411b-4729-9d45-d0ddaba61c41"

async def get_full_models_list():
    """获取完整的模型列表"""
    
    url = "https://ark.cn-beijing.volces.com/api/v3/models"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("🔍 正在获取完整的模型列表...\n")
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                models = data.get("data", [])
                
                print(f"✅ 成功获取模型列表！")
                print(f"总模型数: {len(models)}\n")
                
                # 分类显示模型
                text_models = []
                image_models = []
                other_models = []
                
                for model in models:
                    model_id = model.get("id", "")
                    model_name = model.get("name", "")
                    model_status = model.get("status", "")
                    
                    # 检查是否是生图模型
                    if "seedream" in model_id.lower() or "image" in model_id.lower():
                        image_models.append((model_id, model_name, model_status))
                    elif "doubao" in model_id.lower():
                        text_models.append((model_id, model_name, model_status))
                    else:
                        other_models.append((model_id, model_name, model_status))
                
                # 显示文本/对话模型
                if text_models:
                    print("=" * 80)
                    print("📝 文本/对话模型:")
                    print("=" * 80)
                    for model_id, model_name, model_status in text_models:
                        print(f"  - ID: {model_id}")
                        print(f"    名称: {model_name}")
                        print(f"    状态: {model_status}")
                        print()
                
                # 显示生图模型
                if image_models:
                    print("=" * 80)
                    print("🖼️ 生图模型:")
                    print("=" * 80)
                    for model_id, model_name, model_status in image_models:
                        print(f"  - ID: {model_id}")
                        print(f"    名称: {model_name}")
                        print(f"    状态: {model_status}")
                        print()
                
                # 显示其他模型
                if other_models:
                    print("=" * 80)
                    print("🔧 其他模型:")
                    print("=" * 80)
                    for model_id, model_name, model_status in other_models:
                        print(f"  - ID: {model_id}")
                        print(f"    名称: {model_name}")
                        print(f"    状态: {model_status}")
                        print()
                
                # 检查是否有生图模型
                if not image_models:
                    print("=" * 80)
                    print("⚠️ 警告：未找到生图模型 (seedream)！")
                    print("=" * 80)
                    print("\n这可能意味着：")
                    print("1. 当前 API Key 不支持生图功能")
                    print("2. 需要在火山引擎控制台开通生图服务")
                    print("3. 生图模型在不同的端点或区域")
                    print("\n请访问火山引擎控制台确认：")
                    print("https://console.volcengine.com/ark")
                
                # 保存完整模型列表到文件
                with open("models_list.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print("\n💾 完整模型列表已保存到: models_list.json")
                
            else:
                print(f"❌ 获取模型列表失败")
                print(f"状态码: {response.status_code}")
                print(f"错误: {response.text}")
    
    except Exception as e:
        print(f"❌ 发生异常: {str(e)}")

if __name__ == "__main__":
    asyncio.run(get_full_models_list())
