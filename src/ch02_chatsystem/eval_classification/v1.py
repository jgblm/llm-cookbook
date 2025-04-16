from src.tool.tool import ChatClient


def find_category_and_product_v1(user_input, products_and_category):
    """
    从用户输入中获取到产品和类别

    参数：
    user_input：用户的查询
    products_and_category：产品类型和对应产品的字典
    """

    delimiter = "####"
    system_message = f"""
    您将提供客户服务查询。\
    客户服务查询将用{delimiter}字符分隔。
    输出一个 Python 列表，列表中的每个对象都是 Json 对象，每个对象的格式如下：
        '类别': <电脑和笔记本, 智能手机和配件, 电视和家庭影院系统, \
    游戏机和配件, 音频设备, 相机和摄像机中的一个>,
    以及
        '名称': <必须在下面允许的产品中找到的产品列表>

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

    few_shot_user_1 = """我想要最贵的电脑。"""
    few_shot_assistant_1 = """ 
    [{'category': '电脑和笔记本', \
'products': ['TechPro 超极本', 'BlueWave 游戏本', 'PowerLite Convertible', 'TechPro Desktop', 'BlueWave Chromebook']}]
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{few_shot_user_1}{delimiter}"},
        {'role': 'assistant', 'content': few_shot_assistant_1},
        {'role': 'user', 'content': f"{delimiter}{user_input}{delimiter}"},
    ]
    client = ChatClient()
    return client.get_final_content(messages)

products_and_category = """
    {'电脑和笔记本': ['TechPro 超极本',
  'BlueWave 游戏本',
  'PowerLite Convertible',
  'TechPro Desktop',
  'BlueWave Chromebook'],
 '智能手机和配件': ['SmartX ProPhone'],
 '专业手机': ['MobiTech PowerCase',
  'SmartX MiniPhone',
  'MobiTech Wireless Charger',
  'SmartX EarBuds'],
 '电视和家庭影院系统': ['CineView 4K TV',
  'SoundMax Home Theater',
  'CineView 8K TV',
  'SoundMax Soundbar',
  'CineView OLED TV'],
 '游戏机和配件': ['GameSphere X',
  'ProGamer Controller',
  'GameSphere Y',
  'ProGamer Racing Wheel',
  'GameSphere VR Headset'],
 '音频设备': ['AudioPhonic Noise-Canceling Headphones',
  'WaveSound Bluetooth Speaker',
  'AudioPhonic True Wireless Earbuds',
  'WaveSound Soundbar',
  'AudioPhonic Turntable'],
 '相机和摄像机': ['FotoSnap DSLR Camera',
  'ActionCam 4K',
  'FotoSnap Mirrorless Camera',
  'ZoomMaster Camcorder',
  'FotoSnap Instant Camera']}"""

if __name__ == "__main__":

    # 测试00
    customer_msg_0 = f"""如果我预算有限，我可以买哪款电视？"""
    products_by_category_0 = find_category_and_product_v1(customer_msg_0,products_and_category)
    print(products_by_category_0)

    # 测试01
    customer_msg_1 = f"""我需要一个智能手机的充电器"""
    products_by_category_1 = find_category_and_product_v1(customer_msg_1,products_and_category)
    print(products_by_category_1)

    # 测试02
    customer_msg_2 = f"""你们有哪些电脑？"""
    products_by_category_2 = find_category_and_product_v1(customer_msg_2,products_and_category)
    print(products_by_category_2)

    # 测试03
    customer_msg_3 = f"""
    告诉我关于smartx pro手机和fotosnap相机的信息，那款DSLR的。
    我预算有限，你们有哪些性价比高的电视推荐？"""
    products_by_category_3 = find_category_and_product_v1(customer_msg_3,products_and_category)
    print(products_by_category_3)

    # 测试04
    customer_msg_4 = f"""
    告诉我关于CineView电视的信息，那款8K的，还有Gamesphere游戏机，X款的。
    我预算有限，你们有哪些电脑？"""
    products_by_category_4 = find_category_and_product_v1(customer_msg_4, products_and_category)
    print(products_by_category_4)
