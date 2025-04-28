# 导入文本分割器
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter

chunk_size = 20 #设置块大小
chunk_overlap = 10 #设置块重叠大小

# 初始化递归字符文本分割器
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=["\n\n", "\n", "(?<=\。 )", "！", "？"," "]
)
# 初始化字符文本分割器
c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separator="，"
)

# 初始化token分割器
t_splitter = TokenTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    encoding_name="cl100k_base"
)

if __name__ == "__main__":
    # 中文版
    some_text = """在编写文档时，作者将使用文档结构对内容进行分组。 \
        这可以向读者传达哪些想法是相关的。 例如，密切相关的想法\
        是在句子中。 类似的想法在段落中。 段落构成文档。 \n\n\
        段落通常用一个或两个回车符分隔。 \
        回车符是您在该字符串中看到的嵌入的“反斜杠 n”。 \
        句子末尾有一个句号，但也有一个空格。\
        并且单词之间用空格分隔"""

    print(len(some_text))

    result = t_splitter.split_text(some_text)
    print(result)
