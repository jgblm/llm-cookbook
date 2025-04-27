from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools

from src.ch03_langchain.chat_ai import chatLLM

tools = load_tools(
    ["llm-math", "wikipedia"],
    llm=chatLLM  # 第一步初始化的模型
)

# 初始化代理
agent = initialize_agent(
    tools,  # 第二步加载的工具
    chatLLM,  # 第一步初始化的模型
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # 代理类型
    handle_parsing_errors=True,  # 处理解析错误
    verbose=True  # 输出中间步骤
)

if __name__ == '__main__':
    result = agent.invoke({"input": "Tom M. Mitchell是一位美国计算机科学家，\
    也是卡内基梅隆大学（CMU）的创始人大学教授。他写了哪本书呢？"})
    print(result)
