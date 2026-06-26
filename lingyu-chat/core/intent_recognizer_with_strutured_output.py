from typing import Any

from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from core.prompt import INTEN_RECOGNIZE_WITH_STRUCTURED_OUTPUT_PROMPT


class IntentResult(BaseModel):
    intents: list[str] = Field(description="意图列表，每一个元素为一个意图（支持多意图）")
    slots: dict[str, Any] = Field(description="slot值字典，键为slot名称，值为slot值，从输入中提取的结构化槽位（键值对）")
    score: float = Field(description="置信度分数，意图识别的置信度（0-1），低于阈值可转人工，越大表示越信该意图")


class IntentRecognizer:
    """
    意图识别器：通过大语言模型识别用户输入的意图，输出IntentResult对象
    """

    def __init__(self, llm: ChatTongyi):
        self.__prompt = ChatPromptTemplate.from_messages([
            # MessagesPlaceholder("history"),
            # ("ai","上下文内容:{chat_history}")
            ("system", INTEN_RECOGNIZE_WITH_STRUCTURED_OUTPUT_PROMPT),
            ("ai", "上下文内容:{chat_history}"),
            ("human", "用户输入:{user_input}")
        ])

        self.__structured_llm = llm.with_structured_output(IntentResult)
        self.__chain = self.__prompt | self.__structured_llm

    def recognize(self, user_input: str, chat_history: str | None = None) -> IntentResult:
        # 1.调用llm去识别用户的意图，输入str格式的json字符串
        chat_history = chat_history if chat_history else ""
        result = self.__chain.invoke(input={"chat_history": chat_history, "user_input": user_input})

        # IntentResult result
        if result is None:
            result = IntentResult(
                intents=["general"],
                slots={},
                score=0.0
            )
        return result
