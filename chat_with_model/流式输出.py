import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
    stream = True,
    stream_options = {"include_usage":True}
)

for chunk in completion:
    # print(chunk.model_dump_json())
    if chunk.choices:
        content = chunk.choices[0].delta.content
        if content :
            print(content,
                  end="",  #换行符是“”
                  flush=True  #刷新缓存区
            )
    elif hasattr(chunk,"usage") and chunk.usage:
        print(f"\n\nToken 使用情况：{chunk.usage}")

    # if chunk.choices[0].delta.content:
    #     print(chunk.choices[0].delta.content)
