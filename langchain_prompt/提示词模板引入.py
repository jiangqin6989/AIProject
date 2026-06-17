from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

llm = Tongyi(model="qwen-max")

prompt_template = PromptTemplate.from_template(
    "假设你是一名{export}专家，请你解释一下{content}是什么"
)

prompt = prompt_template.format(export = "AI",content = "大语言模型")

result = llm.stream(prompt)
for chunk in result:
    print(chunk,end="",flush=True)