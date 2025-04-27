from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool

from src.ch03_langchain.chat_ai import chatLLM

agent = create_python_agent(
    chatLLM,  #使用前面一节已经加载的大语言模型
    tool=PythonREPLTool(), #使用Python交互式环境工具 REPLTool
    verbose=True #输出中间步骤
)

if __name__ == '__main__':
    customer_list = ["小明","小黄","小红","小蓝","小橘","小绿",]
    input = f"将使用pinyin拼音库这些客户名字转换为拼音，并打印输出列表: {customer_list}。"
    result = agent.invoke({"input":input})
    print(result)
