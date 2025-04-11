import os
from openai import OpenAI
import dotenv


class ChatClient:
    client = None

    def __init__(self):
        dotenv.load_dotenv("../../.env")
        self.client = OpenAI(
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

    def get_response(self, messages):
        # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        completion = self.client.chat.completions.create(model="qwen-plus-character", messages=messages)
        return completion

    def get_moderation(self, message):
        response = self.client.moderations.create(model="qwen-plus-character",input=message)
        return response
