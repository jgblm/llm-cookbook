from langchain.indexes.vectorstore import VectorStoreIndexWrapper

from src.ch03_langchain.base_document.redis_vector_storage import vector_store

if __name__ == '__main__':
    query = "Please list all your shirts with sun protection \
    in a table in markdown and summarize each one."
    response = vector_store.search(query,search_type="mmr")
    size = len(response)
    print(f'返回的结果条数:{size}')
    for i in range(size):
        print(f'第{i+1}条结果:')
        print(response[i].page_content)
        print('')
