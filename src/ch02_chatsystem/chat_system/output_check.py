# 这是一段电子产品相关的信息
from src.tool.tool import ChatClient

system_message = f"""
您是一个助理，用于评估客服代理的回复是否充分回答了客户问题，\
并验证助理从产品信息中引用的所有事实是否正确。 
产品信息、用户和客服代理的信息将使用三个反引号（即 ```）\
进行分隔。 
请以 Y 或 N 的字符形式进行回复，不要包含标点符号：\
Y - 如果输出充分回答了问题并且回复正确地使用了产品信息\
N - 其他情况。

仅输出单个字母。
"""

product_information = """{ "name": "SmartX ProPhone", "category": "Smartphones and Accessories", "brand": "SmartX", "model_number": "SX-PP10", "warranty": "1 year", "rating": 4.6, "features": [ "6.1-inch display", "128GB storage", "12MP dual camera", "5G" ], "description": "A powerful smartphone with advanced camera features.", "price": 899.99 } { "name": "FotoSnap DSLR Camera", "category": "Cameras and Camcorders", "brand": "FotoSnap", "model_number": "FS-DSLR200", "warranty": "1 year", "rating": 4.7, "features": [ "24.2MP sensor", "1080p video", "3-inch LCD", "Interchangeable lenses" ], "description": "Capture stunning photos and videos with this versatile DSLR camera.", "price": 599.99 } { "name": "CineView 4K TV", "category": "Televisions and Home Theater Systems", "brand": "CineView", "model_number": "CV-4K55", "warranty": "2 years", "rating": 4.8, "features": [ "55-inch display", "4K resolution", "HDR", "Smart TV" ], "description": "A stunning 4K TV with vibrant colors and smart features.", "price": 599.99 } { "name": "SoundMax Home Theater", "category": "Televisions and Home Theater Systems", "brand": "SoundMax", "model_number": "SM-HT100", "warranty": "1 year", "rating": 4.4, "features": [ "5.1 channel", "1000W output", "Wireless subwoofer", "Bluetooth" ], "description": "A powerful home theater system for an immersive audio experience.", "price": 399.99 } { "name": "CineView 8K TV", "category": "Televisions and Home Theater Systems", "brand": "CineView", "model_number": "CV-8K65", "warranty": "2 years", "rating": 4.9, "features": [ "65-inch display", "8K resolution", "HDR", "Smart TV" ], "description": "Experience the future of television with this stunning 8K TV.", "price": 2999.99 } { "name": "SoundMax Soundbar", "category": "Televisions and Home Theater Systems", "brand": "SoundMax", "model_number": "SM-SB50", "warranty": "1 year", "rating": 4.3, "features": [ "2.1 channel", "300W output", "Wireless subwoofer", "Bluetooth" ], "description": "Upgrade your TV's audio with this sleek and powerful soundbar.", "price": 199.99 } { "name": "CineView OLED TV", "category": "Televisions and Home Theater Systems", "brand": "CineView", "model_number": "CV-OLED55", "warranty": "2 years", "rating": 4.7, "features": [ "55-inch display", "4K resolution", "HDR", "Smart TV" ], "description": "Experience true blacks and vibrant colors with this OLED TV.", "price": 1499.99 }"""

client = ChatClient()
response = client.get_final_content(messages)
print(response)


def check_output(input, output):
    q_a_pair = f"""
    顾客的信息: ```{input}```
    产品信息: ```{product_information}```
    代理的回复: ```{output}```

    回复是否正确使用了检索的信息？
    回复是否充分地回答了问题？

    输出 Y 或 N
    """

    # 判断相关性
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': q_a_pair}
    ]
    client = ChatClient()
    response = client.get_final_content(messages)
    print("输出是否与输入关联: {}", response)
    return response
