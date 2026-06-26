import json
import re
from typing import Any
from dataclasses import dataclass

from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from .prompt import INTEN_RECOGNIZE_PROMPT


@dataclass(frozen=True)
class IntentResult:
    """
    --intent: 意图列表，每一个元素为一个意图（支持多意图）
    --slots: slot值字典，键为slot名称，值为slot值，从输入中提取的结构化槽位（键值对）
    --confidence: 置信度分数，意图识别的置信度（0-1），低于阈值可转人工，越大表示越信该意图
    """
    intents: list[str]
    slots: dict[str, Any]
    confidence: float


class IntentRecognizer:
    """
    意图识别器：通过大语言模型识别用户输入的意图，输出IntentResult对象
    """

    def __init__(self, llm: ChatTongyi):
        self.__prompt = ChatPromptTemplate.from_messages([
            # MessagesPlaceholder("history"),
            # ("ai","上下文内容:{chat_history}")
            ("system", INTEN_RECOGNIZE_PROMPT),
            ("ai", "上下文内容:{chat_history}"),
            ("human", "用户输入:{user_input}")
        ])

        self.__llm = llm
        self.__chain = self.__prompt | self.__llm | StrOutputParser()

    def recognize(self, user_input: str, chat_history: str | None = None) -> IntentResult:
        # 1.调用llm去识别用户的意图，输入str格式的json字符串
        chat_history = chat_history if chat_history else ""
        result = self.__chain.invoke(input={"chat_history": chat_history, "user_input": user_input})
        # print(result)

        # 2.解析大模型输出
        # 2.0 将str转化成json(dict)
        data = self.__parse_str_to_json(result)
        # print(data)

        # 2.1解析intents意图
        intents = data.get("intents")
        if not isinstance(intents, list):
            intent = data.get("intent")
            intents = [intent] if isinstance(intent, str) else []
        # print(intents)

        # 2.2 解析slots插槽
        slots = data.get("slots") if isinstance(data.get("slots"), dict) else {}
        # print(slots)

        # 2.3 解析confidence置信度
        try:
            confidence = float(data.get("confidence"))
        except:
            confidence = 0.0
        confidence = max(0.0, min(1.0, confidence))
        # print(confidence)

        # 3.返回结果
        return IntentResult(intents=intents, slots=slots, confidence=confidence)

    def __parse_str_to_json(self, text: str) -> dict[str, Any]:
        if not text or not text.strip():
            return {"intents": ["general"], "slots": {}, "confidence": 0.0}

        # 尝试将text转化成dict
        text = text.strip()
        try:
            return json.loads(text)
        except json.decoder.JSONDecodeError:
            pass

        find_text = re.search(r"{{.*?}}", text, re.DOTALL)
        if find_text:
            try:
                return json.loads(find_text.group(0))
            except json.JSONDecodeError:
                pass

        # 如果未找到json字符串，那么返回默认值
        return {"intents": ["general"], "slots": {}, "confidence": 0.0}
