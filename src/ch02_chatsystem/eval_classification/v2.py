from src.tool.tool import ChatClient
from src.ch02_chatsystem.eval_classification.v1 import products_and_category


def find_category_and_product_v2(user_input, products_and_category):
    """
    从用户输入中获取到产品和类别

    添加：不要输出任何不符合 JSON 格式的额外文本。
    添加了第二个示例（用于 few-shot 提示），用户询问最便宜的计算机。
    在这两个 few-shot 示例中，显示的响应只是 JSON 格式的完整产品列表。

    参数：
    user_input：用户的查询
    products_and_category：产品类型和对应产品的字典
    """
    delimiter = "####"
    system_message = f"""
    您将提供客户服务查询。\
    客户服务查询将用{delimiter}字符分隔。
    输出一个 Python列表，列表中的每个对象都是 JSON 对象，每个对象的格式如下：
        '类别': <电脑和笔记本, 智能手机和配件, 电视和家庭影院系统, \
    游戏机和配件, 音频设备, 相机和摄像机中的一个>,
    以及
        '名称': <必须在下面允许的产品中找到的产品列表>
    不要输出任何不是 JSON 格式的额外文本。
    输出请求的 JSON 后，不要写任何解释性的文本。

    其中类别和产品必须在客户服务查询中找到。
    如果提到了一个产品，它必须与下面允许的产品列表中的正确类别关联。
    如果没有找到产品或类别，输出一个空列表。

    根据产品名称和产品类别与客户服务查询的相关性，列出所有相关的产品。
    不要从产品的名称中假设任何特性或属性，如相对质量或价格。

    允许的产品以 JSON 格式提供。
    每个项目的键代表类别。
    每个项目的值是该类别中的产品列表。
    允许的产品：{products_and_category}

    """

    few_shot_user_1 = """我想要最贵的电脑。你推荐哪款？"""
    few_shot_assistant_1 = """ 
    [{'category': '电脑和笔记本', \
'products': ['TechPro 超极本', 'BlueWave 游戏本', 'PowerLite Convertible', 'TechPro Desktop', 'BlueWave Chromebook']}]
     """

    few_shot_user_2 = """我想要最便宜的电脑。你推荐哪款？"""
    few_shot_assistant_2 = """ 
    [{'category': '电脑和笔记本', \
'products': ['TechPro 超极本', 'BlueWave 游戏本', 'PowerLite Convertible', 'TechPro Desktop', 'BlueWave Chromebook']}]
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{few_shot_user_1}{delimiter}"},
        {'role': 'assistant', 'content': few_shot_assistant_1},
        {'role': 'user', 'content': f"{delimiter}{few_shot_user_2}{delimiter}"},
        {'role': 'assistant', 'content': few_shot_assistant_2},
        {'role': 'user', 'content': f"{delimiter}{user_input}{delimiter}"},
    ]
    client = ChatClient()
    return client.get_final_content(messages)


if __name__ == "__main__":
    #  测试用例03 v1版本结果不理想，修改提示词后再次验证
    customer_msg_3 = f"""
    告诉我关于smartx pro手机和fotosnap相机的信息，那款DSLR的。
    另外，你们有哪些电视？"""
    products_by_category_3 = find_category_and_product_v2(customer_msg_3, products_and_category)
    print(products_by_category_3)

    #  回归测试用例00
    customer_msg_0 = f"""如果我预算有限，我可以买哪款电视？"""
    products_by_category_0 = find_category_and_product_v2(customer_msg_0,products_and_category)
    print(products_by_category_0)
