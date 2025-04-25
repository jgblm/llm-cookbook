from langchain.indexes.vectorstore import VectorStoreIndexWrapper

from src.ch03_langchain.base_document.redis_vector_storage import vector_store
from src.ch03_langchain.chat_ai import chatLLM

if __name__ == "__main__":
    # df = pd.read_csv(file_path, usecols=[1, 2])
    # display(df.head())
    wrapper = VectorStoreIndexWrapper(vectorstore=vector_store)
    query = "请用markdown表格的方式列出所有具有防晒功能的衬衫，对每件衬衫描述进行总结"
    # 使用索引查询创建一个响应，并传入这个查询
    response = wrapper.query(question=query, llm=chatLLM)
    # 查看查询返回的内容
    print(response)
