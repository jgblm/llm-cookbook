from langchain_core.prompts import ChatPromptTemplate

from src.ch03_langchain.base_document.redis_vector_storage import vector_store
from src.ch03_langchain.chat_ai import embeddingLLM, chatLLM

if __name__ == "__main__":
    query = "请推荐一件具有防晒功能的衬衫"
    # 使用上面的向量存储来查找与传入查询类似的文本，得到一个相似文档列表
    docs = vector_store.similarity_search(query)
    # 合并获得的相似文档内容
    qdocs = "".join([docs[i].page_content for i in range(len(docs))])

    prompt = f"""
    基于以下的内容，请回答问题：{query}
    {qdocs}
    """
    prompt_template = ChatPromptTemplate.from_template(prompt)
    chain = prompt_template | chatLLM
    
    response = chain.invoke({"query": query, "qdocs": qdocs})
    print(response.content)
