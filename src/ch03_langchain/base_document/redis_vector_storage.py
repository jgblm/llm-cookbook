import time

from langchain_community.document_loaders import CSVLoader
from langchain_redis import RedisConfig, RedisVectorStore
from langchain_text_splitters import CharacterTextSplitter

from src.ch03_langchain.chat_ai import embeddingLLM

config = RedisConfig(
    index_name="newsgroups",
    redis_url="redis://:123456@localhost:6379",
)

vector_store = RedisVectorStore(embeddings=embeddingLLM, config=config)

if __name__ == "__main__":
    file_path = "../../../content/必修三-LangChain for LLM Application Development/data/OutdoorClothingCatalog_1000.csv"
    # 使用langchain文档加载器对数据进行导入
    loader = CSVLoader(file_path=file_path)
    # df = pd.read_csv(file_path, usecols=[1, 2])
    # display(df.head())
    documents = loader.load()
    # 2. 分割文档
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    start_time = time.time()

    # 5. 创建 RedisVectorStore 实例并为文档创建索引
    RedisVectorStore.from_documents(
        docs,
        embeddingLLM,
        redis_url="redis://:123456@localhost:6379",
        index_name="newsgroups"
    )
    end_time = time.time()
    execute_time = end_time - start_time
    print(f"导入完毕:共耗时{execute_time}秒")
