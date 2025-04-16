import os
import dotenv
from langchain_openai import ChatOpenAI

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path=env_path)
chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus-character",
    # other params...
)