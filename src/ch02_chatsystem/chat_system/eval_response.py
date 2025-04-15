from src.tool.tool import ChatClient


def eval_response(user_input, final_response):
    delimiter = "####"
    system_message = f"""
            您是一家大型电子商店的客户服务助理。\
            请以友好和乐于助人的语气回答问题，并提供简洁明了的答案。\
            请确保向用户提出相关的后续问题。
        """
    user_message = f"""
        用户信息: {delimiter}{user_input}{delimiter}
        代理回复: {delimiter}{final_response}{delimiter}

        回复是否足够回答问题
        如果足够，回答 Y
        如果不足够，回答 N
        仅回答上述字母即可
        """
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': user_message}
    ]
    # 要求模型评估回答
    client = ChatClient()
    evaluation_response = client.get_final_content(messages)
    print("evaluation_response:",evaluation_response)
    return evaluation_response