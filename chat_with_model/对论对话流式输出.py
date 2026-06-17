import os
from openai import OpenAI

class MultiTurnChat:
    def __init__(self, base_url: str, model: str, system_prompt: str = None):
        api_key = os.getenv("DASHSCOPE_API_KEY")
        if not api_key:
            raise ValueError("请先配置环境变量 DASHSCOPE_API_KEY")

        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.chat_history = []

        if system_prompt:
            self.chat_history.append({"role": "system", "content": system_prompt})

    def add_user_message(self, message: str) -> None:
        self.chat_history.append({"role": "user", "content": message})

    def add_assistant_message(self, message: str) -> None:
        self.chat_history.append({"role": "assistant", "content": message})

    def send(self, user_message: str):
        """发送消息"""
        # 1. 添加用户消息到历史
        self.add_user_message(user_message)

        # 2. 调用模型
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.chat_history,
            stream=True
        )

        # 3. 提取模型的回复结果
        # reply = completion.choices[0].message.content  一次性调用
        full_reply = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                full_reply += content
                yield content #逐块返回给调用方

            #     if content:
            #         print(content,
            #               end="",  # 换行符是“”
            #               flush=True  # 刷新缓存区
            #               )
            # elif hasattr(chunk, "usage") and chunk.usage:
            #     print(f"\n\nToken 使用情况：{chunk.usage}")

        # 4. 添加模型的回复到历史
        self.add_assistant_message(full_reply)

        # return reply


if __name__ == "__main__":
    # 1. 配置参数
    BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    MODEL = "qwen-plus"
    SYSTEM_MESSAGE = "背景设定：你现在是一个AI老师，负责上AI课程"

    # 2. 创建多轮对话对象
    chat = MultiTurnChat(
        base_url=BASE_URL,
        model=MODEL,
        system_prompt=SYSTEM_MESSAGE,
    )

    # 3. 打印日志
    print("多轮对话已开启，输入内容后按回车发送，输入 'exit' 或 'quit' 退出程序。\n")

    # 4. 循环接收用户输入并回答
    while True:
        user_input = input("用户：")

        if user_input in ["exit", "quit"]:
            print("对话结束，再见")
            break

        # 跳过空输入
        if not user_input.strip():
            print("请勿输入空白字符！")
            continue

        # 调用模型并回复
        # reply = chat.send(user_input)
        # print(f"AI老师：{reply}")

        print("AI老师：", end="", flush=True)
        for chunk in chat.send(user_input):
            print(chunk, end="", flush=True)
        print()

