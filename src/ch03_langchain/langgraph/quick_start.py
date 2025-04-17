from typing import Annotated

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from src.ch03_langchain.chat_ai import chatLLM


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    return {"messages": [chatLLM.invoke(state["messages"])]}


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            # 访问最后一个消息的内容，并将其打印出来
            print("Assistant:", value["messages"][-1].content)
            # print("Test:", value)


if __name__ == '__main__':
    # 1. 创建一个 StateGraph 对象
    graph_builder = StateGraph(State)

    # 2. 添加 chatbot 节点
    graph_builder.add_node("chatbot", chatbot)

    # 3. 定义 StateGraph 的入口
    graph_builder.set_entry_point("chatbot")

    # 4. 定义 StateGraph 的出口
    graph_builder.set_finish_point("chatbot")

    # 5. 编译成graph
    graph = graph_builder.compile()

    # 6. 可视化 graph
    try:
        graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
    except Exception:
        # This requires some extra dependencies and is optional
        pass

    # 7. 运行 graph
    # 通过输入"quit", "exit", "q"结束对话
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input)
        # 如果在 try 块中的代码执行时发生任何异常，将执行 except 块中的代码
        except:
            # 在异常情况下，这行代码将 user_input 变量设置为一个特定的问题
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(user_input)
            break
