import re
import json

def extract_json(text):
    find_text = re.search(r"{.*?}", text, re.DOTALL)
    if find_text:
        try:
            return json.loads(find_text.group(0))
        except json.JSONDecodeError:
            print(f"'''{text}'''不是一个合法的json格式")
    return None

s1 = '好的，我将直接给你输出json，不输出别的内容：\n {"name":"张三","age":30}更多文本'
print(extract_json(s1))  #{'name': '张三', 'age': 30}

s2 = '数据如下:\n {\n "status":"ok",\n "code": 200\n}\n结束'
print(extract_json(s2))  #{'status': 'ok', 'code': 200}

s3 = '代码块{ var x = 1} 注释'
print(extract_json(s3))
#'''代码块{ var x = 1} 注释'''不是一个合法的json格式
#None

s4 = """
{
  "intents": [
    "general"
  ],
  "slots": {
    "order_id": "0331231dr4fwe8",
    "new_address": null
  },
  "confidence": 0.5
}
"""
print(extract_json(s4))