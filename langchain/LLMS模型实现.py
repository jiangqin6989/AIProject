from langchain_community.chat_models import ChatTongyi

#class ChatTongyi(BaseChatModel):  实现类的包
#class BaseChatModel：    langchain_core 规范！

from langchain_community.llms.tongyi import Tongyi
#class Tongyi(BaseLLM):
#class BaseLLM(BaseLanguageModel[str], ABC) 规范！

from langchain_community.embeddings import DashScopeEmbeddings
#class DashScopeEmbeddings(BaseModel, Embeddings)
#class Embeddings(ABC)  规范！

llm = Tongyi(model = "qwen-max")
result = llm.invoke(input = "你是谁") #一次性获得所有内容一次性输出
print(type(result))  #str
print(result)

llm = Tongyi(model = "qwen-max")
stream = llm.stream(input = "你是谁") #一次性获得所有内容一次性输出
print(type(stream))  #generator
for chunk in stream:
    # print(type(chunk)) #str
    print(chunk,end="",flush=True)