from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# 1、准备示例数据
examples = [
    {"input": "高兴", "output": "愉悦"},
    {"input": "快速", "output": "迅猛"},
    {"input": "美丽", "output": "绚丽"}
]

# 2、构建提示词模板
example_prompt = PromptTemplate.from_template(
    "输入：{input}\n输出：{output}"
)

# 3、创建FewShotPromptTemplate
few_shot_peompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="请根据以下示例，将输入词语转化为同义词",
    suffix="基于示例回答问题，用户输入：{word}\n输出：",
    input_variables=["word"]
)

# 4、调用
# prompt_text = few_shot_peompt.format(word="悲伤")
# print(type(prompt_text))
# print(prompt_text)


# llm = Tongyi(model = "qwen-max")
# chain = few_shot_peompt | llm
# result = chain.invoke(input = {"word":"烦恼"})
# print(type(result))
# print(result)


prompt_text = few_shot_peompt.invoke(input={"word": "悲伤"})
print(type(prompt_text.text))
# print(prompt_text.text)
print(prompt_text.to_string())
