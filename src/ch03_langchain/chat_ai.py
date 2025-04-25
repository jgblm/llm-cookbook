import os

import dotenv
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_openai import ChatOpenAI

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path=env_path)
chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus-character",
    # other params...
)
jsonLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus-character",
    # other params...
).bind(response_format={"type": "json_object"})

embeddingLLM = DashScopeEmbeddings(
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
    model="text-embedding-v3",
)
