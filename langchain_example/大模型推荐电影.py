from langchain_community.chat_models import ChatTongyi
from langchain_community.llms.tongyi import Tongyi
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

prompt1 = PromptTemplate.from_template(
    "根据用户喜欢的电影类型，推荐一部电影并以JSON的格式输出。\n"
    "用户类型：{genre}\n"
    "输出格式：{{\"title\":\"电影名称\", \"director\":\"导演\",\"year\":\"上映时间\",\"reason\":\"推荐理由\"}}"
)

jsonparse = JsonOutputParser()

llm = ChatTongyi(model = "qwen3-max" , streaming = True)  #输出 AIMessage
#
# chain = prompt1 | llm | jsonparse

# result = chain.invoke(input={"genre":"玄幻"})
# print(result)  #{'title': '捉妖记', 'director': '许诚毅', 'year': '2015', 'reason': '《捉妖记》融合了中国传统神话与现代奇幻元素，讲述人与妖怪共存的世界中一段温情又冒险的故事。影片特效精良、想象力丰富，完美契合玄幻题材爱好者对神秘世界和超自然生物的喜好。'}

# result = chain.stream(input={"genre":"玄幻"})
# for chunk in result:
#     print(result,end="",flush=True)

prompt2 = PromptTemplate.from_template(
    "请将以下的电影推荐翻译成英文，只输出翻译结果。\n"
    "电影名称：{title}\n导演：{director}\n上映年份：{year}\n推荐原因：{reason}"
)

strprase = StrOutputParser()

chain = prompt1 | llm | jsonparse | prompt2 | llm | strprase
result = chain.invoke(input={"genre":"玄幻"})
print(result)