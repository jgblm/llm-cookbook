from langchain.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory

from src.ch03_langchain.chat_ai import chatLLM

if __name__ == "__main__":
    prompt = ChatPromptTemplate(
        [
            MessagesPlaceholder("history"),
            HumanMessagePromptTemplate.from_template("{text}"),
        ]
    )
    origin_chain = prompt | chatLLM
    messageHistory = InMemoryChatMessageHistory()
    messageHistory.add_user_message("Hi, my name is Bob")
    memory_chain = RunnableWithMessageHistory(origin_chain,
                                              get_session_history=lambda: messageHistory,
                                              input_messages_key="text",
                                              history_messages_key="history")

    memory_chain.invoke({"text": "1+1=?"})
    memory_chain.invoke({"text": "2+2=?"})
    resp = memory_chain.invoke({"text": "What is my name?"})
    print(resp.content)
    print(messageHistory.messages)
