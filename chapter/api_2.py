import dashscope
from dashscope import Generation

def chat_with_qwen(user_message):
    """与通义千问对话"""
    response = Generation.call(
        model='qwen-turbo',  # 使用turbo模型
        messages=[
            {'role': 'system', 'content': '你是一个helpful助手'},
            {'role': 'user', 'content': user_message}
        ],
        # stream=True,
        temperature=0.7,  # 平衡的创造性
        max_tokens=1000, # 最多生成1000个token
    )

    if response.status_code == 200:
        return response.output.text
        # return response
    else:
        return f"错误：{response.message}"


# 使用示例
result = chat_with_qwen("你是什么，你能干什么,介绍详细一些")
print(result)