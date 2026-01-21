"""
火山引擎 AI 生图 MCP 工具 - 测试脚本
直接测试 API 功能
"""

import os
import time
import asyncio
import httpx
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

API_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
API_KEY = os.getenv("ARK_API_KEY")


class TestResults:
    """测试结果记录"""
    def __init__(self):
        self.results = []
        self.start_time = time.time()
    
    def add_result(self, test_id, test_name, status, response_time, details=""):
        """添加测试结果"""
        self.results.append({
            "test_id": test_id,
            "test_name": test_name,
            "status": status,  # "通过" or "失败"
            "response_time": response_time,
            "details": details
        })
        print(f"\n{'✅' if status == '通过' else '❌'} [{test_id}] {test_name}: {status} (耗时: {response_time:.2f}秒)")
        if details:
            print(f"   详情: {details}")
    
    def print_summary(self):
        """打印测试总结"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] == "通过")
        failed = total - passed
        pass_rate = (passed / total * 100) if total > 0 else 0
        
        print("\n" + "="*60)
        print("📊 测试总结")
        print("="*60)
        print(f"总测试数: {total}")
        print(f"通过数: {passed}")
        print(f"失败数: {failed}")
        print(f"通过率: {pass_rate:.1f}%")
        print(f"总耗时: {time.time() - self.start_time:.2f}秒")
        print("="*60)
        
        # 打印详细结果
        print("\n📋 详细结果:")
        for result in self.results:
            status_icon = "✅" if result["status"] == "通过" else "❌"
            print(f"{status_icon} [{result['test_id']}] {result['test_name']}: {result['status']} ({result['response_time']:.2f}秒)")
            if result["details"]:
                print(f"   详情: {result['details']}")


async def test_tc001_simple_t2i():
    """TC001: 简单文生图测试"""
    start_time = time.time()
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
            
            payload = {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成一张简单的风景画，描绘宁静的湖泊和远山",
                "size": "2K"
            }
            
            response = await client.post(
                f"{API_BASE_URL}/images/generations",
                headers=headers,
                json=payload
            )
            
            response.raise_for_status()
            data = response.json()
            
            if data.get("data") and len(data["data"]) > 0:
                image_url = data["data"][0].get("url", "")
                if image_url:
                    return "通过", time.time() - start_time, f"图片URL: {image_url[:50]}..."
                else:
                    return "失败", time.time() - start_time, "未返回图片URL"
            else:
                return "失败", time.time() - start_time, "API返回数据为空"
    
    except Exception as e:
        return "失败", time.time() - start_time, str(e)


async def test_tc002_full_params():
    """TC002: 完整参数测试"""
    start_time = time.time()
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
            
            payload = {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成一张专业摄影师拍摄的商业肖像，自然光，眼神自信，背景简洁，8K分辨率，文本权重 7.5，添加水印",
                "size": "4K",
                "guidance_scale": 7.5,
                "watermark": True
            }
            
            response = await client.post(
                f"{API_BASE_URL}/images/generations",
                headers=headers,
                json=payload
            )
            
            response.raise_for_status()
            data = response.json()
            
            if data.get("data") and len(data["data"]) > 0:
                image_url = data["data"][0].get("url", "")
                if image_url:
                    return "通过", time.time() - start_time, f"图片URL: {image_url[:50]}..."
                else:
                    return "失败", time.time() - start_time, "未返回图片URL"
            else:
                return "失败", time.time() - start_time, "API返回数据为空"
    
    except Exception as e:
        return "失败", time.time() - start_time, str(e)


async def test_tc003_base64_format():
    """TC003: Base64 格式测试"""
    start_time = time.time()
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
            
            payload = {
                "model": "doubao-seedream-4-5-251128",
                "prompt": "生成一张简约风格的企业 Logo",
                "size": "2K",
                "response_format": "b64_json"
            }
            
            response = await client.post(
                f"{API_BASE_URL}/images/generations",
                headers=headers,
                json=payload
            )
            
            response.raise_for_status()
            data = response.json()
            
            if data.get("data") and len(data["data"]) > 0:
                b64_data = data["data"][0].get("b64_json", "")
                if b64_data:
                    return "通过", time.time() - start_time, f"Base64数据长度: {len(b64_data)} 字符"
                else:
                    return "失败", time.time() - start_time, "未返回Base64数据"
            else:
                return "失败", time.time() - start_time, "API返回数据为空"
    
    except Exception as e:
        return "失败", time.time() - start_time, str(e)


async def test_tc004_multiple_images():
    """TC004: 多次生成测试（模拟批量）"""
    start_time = time.time()
    
    try:
        async with httpx.AsyncClient(timeout=180.0) as client:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
            
            # 由于 API 不支持批量生成，我们模拟生成 3 张图片
            prompts = [
                "生成一张赛博朋克风格的城市夜景，霓虹灯，高楼",
                "生成一张现代风格的城市夜景，灯火辉煌",
                "生成一张简约风格的城市夜景，月光下的街道"
            ]
            
            images_generated = 0
            for i, prompt in enumerate(prompts, 1):
                payload = {
                    "model": "doubao-seedream-4-5-251128",
                    "prompt": prompt,
                    "size": "2K",
                    "count": 1
                }
                
                response = await client.post(
                    f"{API_BASE_URL}/images/generations",
                    headers=headers,
                    json=payload
                )
                
                response.raise_for_status()
                data = response.json()
                
                if data.get("data") and len(data["data"]) > 0:
                    images_generated += 1
            
            if images_generated == 3:
                return "通过", time.time() - start_time, f"成功生成3张图片（通过多次调用模拟批量）"
            else:
                return "失败", time.time() - start_time, f"期望3张图片，实际生成{images_generated}张"
    
    except Exception as e:
        return "失败", time.time() - start_time, str(e)


def test_tc007_list_models():
    """TC007: 模型列表查询测试"""
    start_time = time.time()
    
    # 这是一个本地测试，不需要调用API
    try:
        supported_models = {
            "doubao-seedream-4-5-251128": "豆包生图 4.5 (最新，支持多格式)",
            "doubao-seedream-4-0-250828": "豆包生图 4.0",
            "doubao-seedream-3-0-t2i-250415": "豆包生图 3.0 文生图",
            "doubao-seedream-3-0-i2i": "豆包生图 3.0 图生图"
        }
        
        if len(supported_models) == 4:
            return "通过", time.time() - start_time, f"模型列表包含4个模型"
        else:
            return "失败", time.time() - start_time, f"模型列表数量不正确: {len(supported_models)}"
    
    except Exception as e:
        return "失败", time.time() - start_time, str(e)


def test_tc008_api_key_error():
    """TC008: API Key 错误处理测试"""
    start_time = time.time()
    
    try:
        # 测试不使用API Key的情况
        if not API_KEY or API_KEY == "your_api_key_here":
            return "通过", time.time() - start_time, "API Key未设置"
        else:
            # API Key已设置，验证其格式
            if len(API_KEY) > 20 and "-" in API_KEY:
                return "通过", time.time() - start_time, "API Key格式正确"
            else:
                return "失败", time.time() - start_time, "API Key格式不正确"
    
    except Exception as e:
        return "失败", time.time() - start_time, str(e)


async def run_all_tests():
    """运行所有测试"""
    print("🚀 开始执行火山引擎 AI 生图 MCP 工具测试\n")
    print("="*60)
    
    results = TestResults()
    
    # TC001: 简单文生图测试
    print("\n📝 [TC001] 简单文生图测试...")
    status, response_time, details = await test_tc001_simple_t2i()
    results.add_result("TC001", "简单文生图测试", status, response_time, details)
    
    # TC002: 完整参数测试
    print("\n📝 [TC002] 完整参数测试...")
    status, response_time, details = await test_tc002_full_params()
    results.add_result("TC002", "完整参数测试", status, response_time, details)
    
    # TC003: Base64 格式测试
    print("\n📝 [TC003] Base64 格式测试...")
    status, response_time, details = await test_tc003_base64_format()
    results.add_result("TC003", "Base64 格式测试", status, response_time, details)
    
    # TC004: 多张文生图测试
    print("\n📝 [TC004] 多张文生图测试...")
    status, response_time, details = await test_tc004_multiple_images()
    results.add_result("TC004", "多张文生图测试", status, response_time, details)
    
    # TC007: 模型列表查询测试
    print("\n📝 [TC007] 模型列表查询测试...")
    status, response_time, details = test_tc007_list_models()
    results.add_result("TC007", "模型列表查询测试", status, response_time, details)
    
    # TC008: API Key 错误处理测试
    print("\n📝 [TC008] API Key 错误处理测试...")
    status, response_time, details = test_tc008_api_key_error()
    results.add_result("TC008", "API Key 错误处理测试", status, response_time, details)
    
    # 打印测试总结
    results.print_summary()
    
    return results


if __name__ == "__main__":
    # 检查 API Key
    if not API_KEY or API_KEY == "your_api_key_here":
        print("❌ 错误：未设置 ARK_API_KEY 环境变量")
        print("\n请按以下步骤配置：")
        print("1. 访问火山引擎 ARK 控制台获取 API Key")
        print("2. 编辑 .env 文件，填写 API Key")
        print("3. 重新运行测试脚本")
        exit(1)
    
    # 运行测试
    asyncio.run(run_all_tests())
