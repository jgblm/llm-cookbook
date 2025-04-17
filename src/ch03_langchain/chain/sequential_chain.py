from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from src.ch03_langchain.chat_ai import chatLLM

first_prompt = ChatPromptTemplate.from_template(
    "把下面的评论review翻译成英文:"
    "\n\n{Review}"
)

# chain 1: 输入：Review    输出：英文的 Review
chain_one = RunnablePassthrough.assign(English_Review=first_prompt | chatLLM)

# 子链2
# prompt模板 2: 用一句话总结下面的 review
second_prompt = ChatPromptTemplate.from_template(
    "请你用一句话来总结下面的评论review:"
    "\n\n{English_Review}"
)
# chain 2: 输入：英文的Review   输出：总结
chain_two = RunnablePassthrough.assign(summary=second_prompt | chatLLM)

# 子链3
# prompt模板 3: 下面review使用的什么语言
third_prompt = ChatPromptTemplate.from_template(
    "下面的评论review使用的什么语言，只需要写明言语类型，三个字以内:\n\n{Review}"
)
# chain 3: 输入：Review  输出：语言
chain_three = RunnablePassthrough.assign(language=third_prompt | chatLLM)

# 子链4
# prompt模板 4: 使用特定的语言对下面的总结写一个后续回复
fourth_prompt = ChatPromptTemplate.from_template(
    "使用特定的语言对下面的总结写一个后续回复，"
    "\n\n总结: {summary}\n\n语言: {language}"
)
# chain 4: 输入： 总结, 语言    输出： 后续回复
chain_four = RunnablePassthrough.assign(followup_message=fourth_prompt | chatLLM)

overall_chain = chain_one | chain_two | chain_three | chain_four

if __name__ == "__main__":
    review = """
    Je trouve le goût médiocre. La mousse ne tient pas, c'est bizarre. J'achète les mêmes dans le commerce et le goût est bien meilleur...\nVieux lot ou contrefaçon !?
    """
    response = overall_chain.invoke({"Review": review})
    print(response.get("Review"))
    print(response.get("English_Review").content)
    print(response.get("summary").content)
    print(response.get("language").content)
    print(response.get("followup_message").content)
