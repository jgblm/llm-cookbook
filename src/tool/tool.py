import os

from dotenv import find_dotenv
from openai import OpenAI
import dotenv


class ChatClient:
    client = None

    def __init__(self):
        env_path = find_dotenv()
        dotenv.load_dotenv(dotenv_path=env_path)
        self.client = OpenAI(
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

    def get_response(self, messages,temperature=0):
        # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        completion = self.client.chat.completions.create(model="qwen-plus-character", messages=messages,temperature=temperature)
        return completion

    def get_final_content(self, messages):
        response = self.get_response(messages)
        content = response.choices[0].message.content
        return content

    def get_moderation(self, message):
        response = self.client.moderations.create(model="qwen-plus-character",input=message)
        return response
