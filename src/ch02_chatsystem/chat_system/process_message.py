from src.ch02_chatsystem.chat_system import input_check
from src.ch02_chatsystem import prompt_chain
from src.tool.tool import ChatClient
from src.ch02_chatsystem import self_moderation_output
from src.ch02_chatsystem.chat_system import eval_response


def process_message_all(user_message):
    illegal = input_check.check_prompt_injection(user_message)
    if illegal == 'Y':
        raise Exception("illegal input")

    # 处理用户信息
    messages,_ = prompt_chain.process_message(user_message)
    client = ChatClient()
    assistant_response = client.get_final_content(messages)
    messages.append({'role': 'assistant', 'content': assistant_response})

    relation = self_moderation_output.check_relation(user_message, assistant_response)
    if "N" == relation:
        print("抱歉，我们不能提供该信息")
        raise Exception("stop chat")
    eval_result = eval_response.eval_response(user_message, assistant_response)
    if "N" == eval_result:
        print("很抱歉，我无法提供您所需的信息。我将为您转接到一位人工客服代表以获取进一步帮助。")
        raise Exception("stop chat")
    print(assistant_response)


if __name__ == '__main__':
    user_message = f"""
         请告诉我关于 smartx pro phone 和 the fotosnap camera 的信息。
         另外，请告诉我关于你们的tvs的情况。 """
    process_message_all(user_message)
