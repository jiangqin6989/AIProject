from langchain_community.embeddings import DashScopeEmbeddings

#向量化的文本
user_query = "特朗普上一次访华是什么时候？"

#创建嵌入模型对象
#默认使用text-embedding-v1模型
# embedding_model = DashScopeEmbeddings()
embedding_model = DashScopeEmbeddings(model="text-embedding-v3")

#向量化将user_query转化成向量
vector = embedding_model.embed_query(user_query)

print(vector)
print(len(vector))

