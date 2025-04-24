from typing import Literal

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict

from src.ch03_langchain.chat_ai import chatLLM, jsonLLM
import json

llm = chatLLM

# Define the prompts we will route to
prompt_1 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert on animals."),
        ("human", "{input}"),
    ]
)
prompt_2 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert on vegetables."),
        ("human", "{input}"),
    ]
)

# Construct the chains we will route to. These format the input query
# into the respective prompt, run it through a chat model, and cast
# the result to a string.
chain_1 = prompt_1 | llm | StrOutputParser()
chain_2 = prompt_2 | llm | StrOutputParser()

# Next: define the chain that selects which branch to route to.
# Here we will take advantage of tool-calling features to force
# the output to select one of two desired branches.
route_system = "Route the user's query to either the animal or vegetable expert. output format should be json. for example: {{'destination':'animal'}}"
route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", route_system),
        ("human", "{input}")
    ]
)
route_chain = route_prompt | jsonLLM


# For LangGraph, we will define the state of the graph to hold the query,
# destination, and final answer.
class State(TypedDict):
    query: str
    destination: Literal["animal", "vegetable"]
    answer: str


# We define functions for each node, including routing the query:
def route_query(state: State, config: RunnableConfig):
    destination = route_chain.invoke(state["query"], config)
    response = json.loads(destination.content)
    return {"destination": response['destination']}


# And one node for each prompt
def prompt_1(state: State, config: RunnableConfig):
    print("current animal")
    return {"answer": chain_1.invoke(state["query"], config)}


def prompt_2(state: State, config: RunnableConfig):
    print("current vegetable")
    return {"answer": chain_2.invoke(state["query"], config)}


# We then define logic that selects the prompt based on the classification
def select_node(state: State) -> Literal["prompt_1", "prompt_2"]:
    if state["destination"] == "animal":
        return "prompt_1"
    else:
        return "prompt_2"


# Finally, assemble the multi-prompt chain. This is a sequence of two steps:
# 1) Select "animal" or "vegetable" via the route_chain, and collect the answer
# alongside the input query.
# 2) Route the input query to chain_1 or chain_2, based on the
# selection.
graph = StateGraph(State)
graph.add_node("route_query", route_query)
graph.add_node("prompt_1", prompt_1)
graph.add_node("prompt_2", prompt_2)

graph.add_edge(START, "route_query")
graph.add_conditional_edges("route_query", select_node)
graph.add_edge("prompt_1", END)
graph.add_edge("prompt_2", END)
app = graph.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")

if __name__ == "__main__":
    state = app.invoke({"query": "豹子身上有多少个点"})
    print(state["destination"])
    print(state["answer"])
