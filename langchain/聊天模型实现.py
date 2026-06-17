from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage,ToolMessage

#class ChatTongyi(BaseChatModel):  实现类的包
#class BaseChatModel：    langchain_core 规范！

#system、user、assistant、tool、function  （0penAI)

#SystemMessage、HuamnMessage、AIMessage、ToolMessage  (LangChain)

chat = ChatTongyi(model = "qwen3-max",streaming = True)
chat_history = [
    SystemMessage(content="背景设定：你现在是一个AI老师，负责上AI课程"),
    HumanMessage(content="你是谁")
]

# result = chat.invoke(input = chat_history)
# print(type(result))  #langchain_core.messages.ai.AIMessage
# print(result)

result = chat.stream(input = chat_history)
# print(type(result))  #generator
for chunk in result:
    # print(type(chunk))  #langchain_core.messages.ai.AIMessage
    print(chunk.content,end="",flush=True)