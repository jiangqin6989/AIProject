import  numpy as np
from langchain_community.embeddings import DashScopeEmbeddings

def euclidean_distance(a,b):
    return np.linalg.norm(np.array(a)- np.array(b))


if __name__ == '__main__':
    texts = ["猫坐在垫子上","一只猫在垫子上休息","今天天气很好"]
    embedding = DashScopeEmbeddings()

    vectors = embedding.embed_documents(texts)

    #计算欧式距离
    print(f"'{texts[0]}'与'{texts[1]}' 的欧式距离是:{euclidean_distance(vectors[0],vectors[1])}'")
    print(f"'{texts[1]}'与'{texts[2]}' 的欧式距离是:{euclidean_distance(vectors[1],vectors[2])}'")
    print(f"'{texts[0]}'与'{texts[2]}' 的欧式距离是:{euclidean_distance(vectors[0],vectors[2])}'")