from langchain_community.chat_models import ChatTongyi
class MultiTurnChat:
    def __init__(self,model:str,system_prompt:str=None) ->None:
        self.llm =  ChatTongyi(
        model=model,
        streaming = True
        )
        self.chat_history = []
        if system_prompt:
            self.chat_history.append(("system", system_prompt))

    def add_user_message(self,content:str) -> None:
        self.chat_history.append(("human", content))

    def add_ai_message(self, content: str) -> None:
        self.chat_history.append(("ai", content))

    def send(self,user_mesage:str):
        self.add_user_message(user_mesage)
        result = self.llm.stream(input=self.chat_history)
        full_reply = ""
        for chunk in result:
            if chunk.content:
                full_reply += chunk.content
                yield chunk.content

        self.add_ai_message(full_reply)


if __name__ == '__main__':
    MODEL = "qwen-plus"
    SYSTEM_MESSAGE = "背景设定：你现在是一个AI老师，负责上AI课程"

    chat = MultiTurnChat(MODEL,SYSTEM_MESSAGE)

    print("多轮对话已开启，输入内容后按回车发送，输入 'exit' 或 'quit' 退出程序。\n")

    while True:
        user_mesage = input("human:")
        if not user_mesage.strip():
            print("请勿输入空白字符！")
            continue
        if user_mesage in ["exit", "quit"]:
            print("对话结束，再见")
            break

        print("AI老师：", end="", flush=True)

        for chunk in chat.send(user_mesage):
            print(chunk, end="", flush=True)

        print()


















