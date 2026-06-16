from dashscope import Generation

responses = Generation.call(
    model='qwen-turbo',
    messages=[{'role': 'user', 'content': '讲个故事'}],
    stream=True
)

for response in responses:
    if response.output.text:
        print(response.output.text, end='')