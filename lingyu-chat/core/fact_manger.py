from typing import Dict

_facts_store :Dict[str,Dict[str,str]] = {}

class FactManger:
    """负责关键事实（slots）的存储和更新"""
    def __init__(self, chat_session_id:str) -> None:
        self.chat_session_id = chat_session_id
        # 初始化事实存储
        if chat_session_id not in _facts_store:
            _facts_store[chat_session_id] = {}

    def get_all_facts(self) -> Dict[str, str]:
        """获取当前会话的所有关键事实"""
        return _facts_store.get(self.chat_session_id, {}).copy()

    def get_fact(self,key:str) -> str:
        """获取单个事实的值"""
        return _facts_store.get(self.chat_session_id, {}).get(key,{})

    def update_fact(self,facts:Dict[str,str]) -> None:
        """更新关键事实（合并）"""
        if self.chat_session_id not in _facts_store:
            _facts_store[self.chat_session_id] = {}
        # 过滤掉空值
        _facts_store[self.chat_session_id].update({
            k: v for k, v in facts.items() if v
        })
        print("update key facts")

    def set_fact(self,key:str,value:str) -> None:
        """设置单个事实"""
        if self.chat_session_id not in _facts_store:
            _facts_store[self.chat_session_id] = {}
        if value:
            _facts_store[self.chat_session_id][key] = value

