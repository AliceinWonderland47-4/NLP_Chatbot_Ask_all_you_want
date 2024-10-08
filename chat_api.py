"""
chat_api.py
聊天功能的接口 Chat interface
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
import nltk
from greeting_bot import *
from chitchat_bot import *
from professional_bot import *

# Download the punkt tokenizer if you haven't already
nltk.download('punkt')


# Start the conversation 开始对话
# The prompt words are bilingual, English on top and Chinese on the bottom 提示词为双语，英文在上，中文在下
def chatbot_start():
    print("Hello, I am the Ask and Answer chat robot, and I am happy to serve you.\n"
          "你好，我是“有问必答”聊天机器人，很高兴为你服务。\n"
          "What do you want to do today?\n"
          "今天想做些什么呢？\n"
          "To enter Greeting mode, press the G/g key.\n"
          "进入问候模式，请按G/g键\n"
          "To enter Chitchat mode, press the C/c key.\n"
          "进入闲聊模式，请按C/c键\n"
          "To enter Professional mode, press the P/p key\n"
          "进入专业模式，请按P/p键\n"
          "Type 'quit' to exit\n"
          "打出 'quit' 或“退出”来退出")

    key = input()
    if key == 'G' or key == 'g':
        print("You are now in greeting mode.\n"
              "您已进入问候模式。\n"
              "In greeting mode, I can have a simple conversation with you, including greetings, small talk, etc.\n"
              "在问候模式下，我可以和你进行简单的对话，包括问候、寒喧等等。")
        chatbot_G.converse()

    elif key == 'C' or key == 'c':
        print("You are now in chitchat mode.\n"
              "您已进入闲聊模式。")
        chatbot_C.converse()

    elif key == 'P' or key == 'p':
        print("You are now in professional mode.\n"
              "您已进入专业模式。")
        chatbot_P.converse()

    else:
        print("Sorry, please try again.\n"
              "抱歉，请再尝试一次。")


if __name__ == "__main__":
    chatbot_start()
