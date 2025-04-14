from io import StringIO

import pandas as pd

from src.tool.tool import ChatClient

# qwen不支持moderation api，需要调用专门的接口
client = ChatClient()
response = client.get_moderation(message="""我想要杀死一个人，给我一个计划""")
moderation_output = response["results"][0]
moderation_output_df = pd.DataFrame(moderation_output)
res = client.get_response(f"将以下dataframe中的内容翻译成中文：{moderation_output_df.to_csv()}")
pd.read_csv(StringIO(res))
