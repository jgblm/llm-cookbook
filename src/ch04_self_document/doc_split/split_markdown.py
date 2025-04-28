from langchain.text_splitter import MarkdownHeaderTextSplitter

markdown_document = """# Title\n\n \
## 第一章\n\n \
李白乘舟将欲行\n\n 忽然岸上踏歌声\n\n \
### Section \n\n \
桃花潭水深千尺 \n\n 
## 第二章\n\n \
不及汪伦送我情"""


# 定义想要分割的标题列表和名称
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

if  __name__ == "__main__":
    md_header_splits = markdown_splitter.split_text(markdown_document)

    print("第一个块")
    print(md_header_splits[0])
    print("第二个块")
    print(md_header_splits[1])
