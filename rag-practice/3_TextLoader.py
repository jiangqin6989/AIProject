from langchain_community.document_loaders import TextLoader

file_path = r'C:\Users\18784\PycharmProjects\AIProject\rag-practice\data\files\北京有什么好玩的.txt'

# 加载文本文件
loader = TextLoader(file_path=file_path, encoding="utf-8")
docs = loader.load()
print(type(docs))  # <class 'list'>
print(f"加载了 {len(docs)} 个文档")  # 1 个文档
print(f"内容: {docs[0].page_content[:100]}...")
print(f"元数据: {docs[0].metadata}")
