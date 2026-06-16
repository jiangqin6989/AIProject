import dashscope
from dashscope import Generation
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

# 设置API Key
dashscope.api_key = api_key

# 调用通义千问
response = Generation.call(
    model='qwen-turbo',  # 或 qwen-plus, qwen-max
    messages=[
        {'role': 'system', 'content': '你是一个helpful助手'},
        {'role': 'user', 'content': '什么是人工智能？'}
    ]
)

# 打印结果
print(response.output.text)