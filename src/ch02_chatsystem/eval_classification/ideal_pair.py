import json
import time

from src.ch02_chatsystem.eval_classification import v2
from src.ch02_chatsystem.eval_classification.v2 import find_category_and_product_v2

msg_ideal_pairs_set = [

    # eg 0
    {'customer_msg': """如果我预算有限，我可以买哪种电视？""",
     'ideal_answer': {
         '电视和家庭影院系统': set(
             ['CineView 4K TV', 'SoundMax Home Theater', 'CineView 8K TV', 'SoundMax Soundbar', 'CineView OLED TV']
         )}
     },

    # eg 1
    {'customer_msg': """我需要一个智能手机的充电器""",
     'ideal_answer': {
         '智能手机和配件': set(
             ['MobiTech PowerCase', 'MobiTech Wireless Charger', 'SmartX EarBuds']
         )}
     },
    # eg 2
    {'customer_msg': f"""你有什么样的电脑""",
     'ideal_answer': {
         '电脑和笔记本': set(
             ['TechPro 超极本', 'BlueWave 游戏本', 'PowerLite Convertible', 'TechPro Desktop', 'BlueWave Chromebook'
              ])
     }
     },

    # eg 3
    {'customer_msg': f"""告诉我关于smartx pro手机和fotosnap相机的信息，那款DSLR的。\
另外，你们有哪些电视？""",
     'ideal_answer': {
         '智能手机和配件': set(
             ['SmartX ProPhone']),
         '相机和摄像机': set(
             ['FotoSnap DSLR Camera']),
         '电视和家庭影院系统': set(
             ['CineView 4K TV', 'SoundMax Home Theater', 'CineView 8K TV', 'SoundMax Soundbar', 'CineView OLED TV'])
     }
     },

    # eg 4
    {'customer_msg': """告诉我关于CineView电视，那款8K电视、\
     Gamesphere游戏机和X游戏机的信息。我的预算有限，你们有哪些电脑？""",
     'ideal_answer': {
         '电视和家庭影院系统': set(
             ['CineView 8K TV']),
         '游戏机和配件': set(
             ['GameSphere X']),
         '电脑和笔记本': set(
             ['TechPro Ultrabook', 'BlueWave Gaming Laptop', 'PowerLite Convertible', 'TechPro Desktop',
              'BlueWave Chromebook'])
     }
     },

    # eg 5
    {'customer_msg': f"""你们有哪些智能手机""",
     'ideal_answer': {
         '智能手机和配件': set(
             ['SmartX ProPhone', 'MobiTech PowerCase', 'SmartX MiniPhone', 'MobiTech Wireless Charger', 'SmartX EarBuds'
              ])
     }
     },
    # eg 6
    {'customer_msg': f"""我预算有限。你能向我推荐一些智能手机吗？""",
     'ideal_answer': {
         '智能手机和配件': set(
             ['SmartX EarBuds', 'SmartX MiniPhone', 'MobiTech PowerCase', 'SmartX ProPhone',
              'MobiTech Wireless Charger']
         )}
     },

    # eg 7 # this will output a subset of the ideal answer
    {'customer_msg': f"""有哪些游戏机适合我喜欢赛车游戏的朋友？""",
     'ideal_answer': {
         '游戏机和配件': set([
             'GameSphere X',
             'ProGamer Controller',
             'GameSphere Y',
             'ProGamer Racing Wheel',
             'GameSphere VR Headset'
         ])}
     },
    # eg 8
    {'customer_msg': f"""送给我摄像师朋友什么礼物合适？""",
     'ideal_answer': {
         '相机和摄像机': set([
             'FotoSnap DSLR Camera', 'ActionCam 4K', 'FotoSnap Mirrorless Camera', 'ZoomMaster Camcorder',
             'FotoSnap Instant Camera'
         ])}
     },

    # eg 9
    {'customer_msg': f"""我想要一台热水浴缸时光机""",
     'ideal_answer': []
     }

]


def eval_response_with_ideal(response,
                             ideal,
                             debug=False):
    """
    评估回复是否与理想答案匹配

    参数：
    response: 回复的内容
    ideal: 理想的答案
    debug: 是否打印调试信息
    """
    if debug:
        print("回复：")
        print(response)

    # json.loads() 只能解析双引号，因此此处将单引号替换为双引号
    json_like_str = response.replace("'", '"')

    # 解析为一系列的字典
    l_of_d = json.loads(json_like_str)

    # 当响应为空，即没有找到任何商品时
    if l_of_d == [] and ideal == []:
        return 1

    # 另外一种异常情况是，标准答案数量与回复答案数量不匹配
    elif l_of_d == [] or ideal == []:
        return 0

    # 统计正确答案数量
    correct = 0

    if debug:
        print("l_of_d is")
        print(l_of_d)

    # 对每一个问答对
    for d in l_of_d:

        # 获取产品和目录
        cat = d.get('category')
        prod_l = d.get('products')
        # 有获取到产品和目录
        if cat and prod_l:
            # convert list to set for comparison
            prod_set = set(prod_l)
            # get ideal set of products
            ideal_cat = ideal.get(cat)
            if ideal_cat:
                prod_set_ideal = set(ideal.get(cat))
            else:
                if debug:
                    print(f"没有在标准答案中找到目录 {cat}")
                    print(f"标准答案: {ideal}")
                continue

            if debug:
                print("产品集合：\n", prod_set)
                print()
                print("标准答案的产品集合：\n", prod_set_ideal)

            # 查找到的产品集合和标准的产品集合一致
            if prod_set == prod_set_ideal:
                if debug:
                    print("正确")
                correct += 1
            else:
                print("错误")
                print(f"产品集合: {prod_set}")
                print(f"标准的产品集合: {prod_set_ideal}")
                if prod_set <= prod_set_ideal:
                    print("回答是标准答案的一个子集")
                elif prod_set >= prod_set_ideal:
                    print("回答是标准答案的一个超集")

    # 计算正确答案数
    pc_correct = correct / len(l_of_d)

    return pc_correct

if __name__ == '__main__':
    score_accum = 0
    for i, pair in enumerate(msg_ideal_pairs_set):
        time.sleep(20)
        print(f"示例 {i}")

        customer_msg = pair['customer_msg']
        ideal = pair['ideal_answer']

        # print("Customer message",customer_msg)
        # print("ideal:",ideal)
        response = find_category_and_product_v2(customer_msg,
                                                v2.products_and_category)

        # print("products_by_category",products_by_category)
        score = eval_response_with_ideal(response, ideal, debug=True)
        print(f"{i}: {score}")
        score_accum += score

    n_examples = len(msg_ideal_pairs_set)
    fraction_correct = score_accum / n_examples
    print(f"正确比例为 {n_examples}: {fraction_correct}")

