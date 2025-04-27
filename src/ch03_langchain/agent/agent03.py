# 导入tool函数装饰器
from langchain.agents import tool, initialize_agent, AgentType
from datetime import date

from src.ch03_langchain.chat_ai import chatLLM


@tool
def time(text: str) -> str:
    """
    返回今天的日期，用于任何需要知道今天日期的问题。\
    输入应该总是一个空字符串，\
    这个函数将总是返回今天的日期，任何日期计算应该在这个函数之外进行。
    """
    return str(date.today())


# 初始化代理
agent = initialize_agent(
    tools=[time],  # 将刚刚创建的时间工具加入代理
    llm=chatLLM,  # 初始化的模型
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # 代理类型
    handle_parsing_errors=True,  # 处理解析错误
    verbose=True  # 输出中间步骤
)

if __name__ == '__main__':
    # 使用代理询问今天的日期.
    # 注: 代理有时候可能会出错（该功能正在开发中）。如果出现错误，请尝试再次运行它。
    result = agent.invoke({"input": "今天的日期是？"})
    print(result)
