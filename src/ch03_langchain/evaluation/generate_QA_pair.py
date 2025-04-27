import langchain
from langchain.evaluation.qa import QAGenerateChain
from langchain_community.document_loaders import CSVLoader

from src.ch03_langchain.chat_ai import chatLLM
from src.ch03_langchain.evaluation.index import file_path


if __name__ == '__main__':
    loader = CSVLoader(file_path=file_path)
    data = loader.load()
    # 使用llm生成QA
    example_gen_chain = QAGenerateChain.from_llm(llm=chatLLM)
    examples = example_gen_chain.apply([{"doc": t} for t in data[:5]])
    print(examples)
