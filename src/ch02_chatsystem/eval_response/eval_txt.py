
from src.ch02_chatsystem.prompt_chain import process_message
from src.tool.tool import ChatClient


def eval_with_rubric(test_set, assistant_answer):
    """
    使用 GPT API 评估生成的回答

    参数：
    test_set: 测试集
    assistant_answer: 助手的回复
    """

    cust_msg = test_set['customer_msg']
    context = test_set['context']
    completion = assistant_answer

    # 人设
    system_message = """\
    你是一位助理，通过查看客户服务代理使用的上下文来评估客户服务代理回答用户问题的情况。
    """

    # 具体指令
    user_message = f"""\
    你正在根据代理使用的上下文评估对问题的提交答案。以下是数据：
    [开始]
    ************
    [用户问题]: {cust_msg}
    ************
    [使用的上下文]: {context}
    ************
    [客户代理的回答]: {completion}
    ************
    [结束]

    请将提交的答案的事实内容与上下文进行比较，忽略样式、语法或标点符号上的差异。
    回答以下问题：
    助手的回应是否只基于所提供的上下文？（是或否）
    回答中是否包含上下文中未提供的信息？（是或否）
    回应与上下文之间是否存在任何不一致之处？（是或否）
    计算用户提出了多少个问题。（输出一个数字）
    对于用户提出的每个问题，是否有相应的回答？
    问题1：（是或否）
    问题2：（是或否）
    ...
    问题N：（是或否）
    在提出的问题数量中，有多少个问题在回答中得到了回应？（输出一个数字）
"""

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': user_message}
    ]

    client = ChatClient()
    response = client.get_final_content(messages)
    return response


if __name__ == '__main__':
    user_message_1 = f"""
             请告诉我关于 smartx pro phone 和 the fotosnap camera 的信息。
             另外，请告诉我关于你们的tvs的情况。 """
    (messages,product_info) = process_message(user_message_1)
    client = ChatClient()
    assistant_answer = client.get_final_content(messages)
    # 问题、上下文
    cust_prod_info = {
        'customer_msg': user_message_1,
        'context': product_info
    }
    evaluation_output = eval_with_rubric(cust_prod_info, assistant_answer)
    print(evaluation_output)
