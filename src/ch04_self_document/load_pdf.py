from langchain_community.document_loaders import PyPDFLoader

if __name__ == "__main__":
    file_path = "../../content/必修四-LangChain Chat with Your Data/docs/matplotlib/第一回：Matplotlib初相识.pdf"
    # 使用langchain文档加载器对数据进行导入
    loader = PyPDFLoader(file_path=file_path)
    pages = loader.load()

    print(type(pages))
    print(len(pages))

    page = pages[0]
    print(type(page))

    print(page.page_content[0:500])

    print(page.metadata)
