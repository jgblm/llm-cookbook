from langchain.prompts import ChatPromptTemplate

from src.ch03_langchain.chat_ai import chatLLM

# 首先，构造一个提示模版字符串：`template_string`
template_string = """把由三个反引号分隔的文本\
翻译成一种{style}风格。\
文本: ```{text}```
"""

# 然后，我们调用`ChatPromptTemplatee.from_template()`函数将
# 上面的提示模版字符`template_string`转换为提示模版`prompt_template`

prompt_template = ChatPromptTemplate.from_template(template_string)


customer_style = """粤语 \
用一个平静、尊敬的语气
"""

customer_email = """
嗯呐，我现在可是火冒三丈，我那个搅拌机盖子竟然飞了出去，把我厨房的墙壁都溅上了果汁！
更糟糕的是，保修条款可不包括清理我厨房的费用。
伙计，赶紧给我过来！
"""

# 使用提示模版
customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)


if __name__ == "__main__":
    chain = prompt_template | chatLLM
    response = chain.invoke({"style": customer_style, "text": customer_email})
    print(response.content)
