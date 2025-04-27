import langchain.docstore
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.evaluation import QAEvalChain
from langchain.evaluation.qa import QAGenerateChain
from langchain_community.document_loaders import CSVLoader

from src.ch03_langchain.chat_ai import chatLLM
from src.ch03_langchain.evaluation.index import vector_store_test2, file_path

examples = [
    {
        "query": "高清电视机怎么进行护理？",
        "answer": "使用干布清洁。"
    },
    {
        "query": "旅行背包有内外袋吗？",
        "answer": "有。"
    }
]

# 通过指定语言模型、链类型、检索器和我们要打印的详细程度来创建检索QA链
qa = RetrievalQA.from_chain_type(
    llm=chatLLM,
    chain_type="stuff",
    retriever=vector_store_test2.as_retriever(),
    verbose=True,
    chain_type_kwargs={
        "document_separator": "<<<<>>>>>"
    }
)

if __name__ == '__main__':
    loader = CSVLoader(file_path=file_path)
    data = loader.load()
    # QA生成链
    example_gen_chain = QAGenerateChain.from_llm(llm=chatLLM)
    qa_pairs = example_gen_chain.apply([{"doc": t} for t in data[:5]])
    examples.extend([item["qa_pairs"] for item in qa_pairs])
    print(examples)

    # 使用qa链进行问答
    inputs = [item["query"] for item in examples]
    predictions = qa.batch(inputs)

    # QA评估链
    eval_chain = QAEvalChain.from_llm(chatLLM)
    # 在此链上调用evaluate，进行评估
    graded_outputs = eval_chain.evaluate(examples=examples, predictions=predictions)
    print(graded_outputs)

    # 我们将传入示例和预测，得到一堆分级输出，循环遍历它们打印答案
    for i, eg in enumerate(examples):
        print(f"Example {i}:")
        print("Question: " + predictions[i]['query'])
        print("Real Answer: " + examples[i]['answer'])
        print("Predicted Answer: " + predictions[i]['result'])
        print("Predicted Grade: " + graded_outputs[i]['results'])
        print()

