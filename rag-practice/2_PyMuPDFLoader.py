from langchain_community.document_loaders import PyMuPDFLoader

file_path = r'C:\Users\18784\PycharmProjects\AIProject\rag-practice\data\files\sample_document.pdf'

loader = PyMuPDFLoader(file_path=file_path)
# 1.load() 一次性加载所有文档
docs = loader.load()
print(type(docs)) # <class 'list'>
print(type(docs[0])) # Document
print(len(docs)) # 6
print(docs) # [Document(metadata={'producer': 'Skia/PDF m119', 'creator': 'Chromium', 'creationdate':

# 2.lazy_load()：惰性加载
for document in loader.lazy_load():
    print(document.metadata)
