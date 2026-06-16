from langchain_community.document_loaders import PyMuPDFLoader

file_path = "C:/Users/18784/PycharmProjects/AIProject/memory/data/sample_document.pdf"

docs = PyMuPDFLoader(file_path).load()
for doc in docs:
    print(doc.page_content)