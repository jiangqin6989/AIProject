from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

chat_history = []

user_message_1 = "你好，我是一名正在学习ai技术的程序员，我叫小明？"
chat_history.append({"role": "user" , "content": user_message_1})
completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen-plus",
    messages = chat_history
)
print(completion.choices[0].message.content)
chat_history.append({"role": "assistant" , "content": completion.choices[0].message.content})

user_message_2 = "我是谁？"
chat_history.append({"role": "user" , "content": user_message_2})
completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen-plus",
    messages= chat_history
)

print("第二次调用")
print(completion.choices[0].message.content)