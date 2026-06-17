from langchain_community.embeddings import  DashScopeEmbeddings

embedding = DashScopeEmbeddings()

# text = "内容"
# vector = embedding.embed_query(text)
# print(type(vector))
# print(len(vector)) #1536
# print(vector)

texts =["你好","你好小明","你太好了小明"]
vectors = embedding.embed_documents(texts)
print(type(vectors))
print(len(vectors))
print(vectors)
print(vectors[0])
print(vectors[1])
print(vectors[2])
for vector in vectors:
    print(vector)