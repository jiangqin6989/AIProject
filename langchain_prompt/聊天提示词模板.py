from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


def MessagePlacehold(param):
    pass


chat_prompt_template = ChatPromptTemplate.from_messages([
    # ("system","假设你是一个{export}专家"),
    ("system","假设你是一个AI专家"),
    MessagesPlaceholder("history"),
    # ("human","请你解释一下{content}是什么。")
    ("human","我刚刚问了什么内容。")
])

# chat_prompt = chat_prompt_template.format(export="AI",content="langgraph")
# print(type(chat_prompt))
# print(chat_prompt)

# chat_prompt = chat_prompt_template.invoke(input ={"export" : "AI","content" : "langgraph"}).to_string()
# print(type(chat_prompt))
# print(chat_prompt)

chat_history = [
    ("human","什么是langgraph"),
    ("ai","LangGraph是一种结合了自然语言处理（NLP）技术和图数据结构的创新方法，它旨在通过将文本信息转换成图形表示来更好地理解和分析复杂的文本数据。在LangGraph中，文本中的实体（如人名、地点、组织等）被识别并作为节点加入到图中，而这些实体之间的关系则构成图中的边。这种方法允许我们从一个新的视角去探索和理解文本内容，尤其是在处理那些包含丰富语义关系的信息时特别有用。")
]

llm = Tongyi(model = "qwen-max")
chain = chat_prompt_template | llm
# result = chain.stream(input ={"export": "AI","content": "langgraph"})
result = chain.stream(input ={"history": chat_history})
for chunk in result:
    print(chunk,end="",flush=True)