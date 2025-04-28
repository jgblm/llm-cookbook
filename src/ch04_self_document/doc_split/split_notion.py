#加载数据库的内容
from langchain_community.document_loaders import NotionDirectoryLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]
#加载文档分割器
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

if __name__ == "__main__":
    loader = NotionDirectoryLoader("../../../content/必修四-LangChain Chat with Your Data/docs/Notion_DB")
    docs = loader.load()
    txt = ' '.join([d.page_content for d in docs])  # 拼接文档
    md_header_splits = markdown_splitter.split_text(txt)#分割文本内容

    print(md_header_splits[0])#分割结果
