"""
chat_api.py
聊天功能的接口 Chat interface
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
# NLTK自然语言处理库 NLTK Natural Language Processing Library
import nltk
# 5种功能模式 5 function modes
from greeting_bot import *
from chitchat_bot import *
from professional_bot import *
from nonsense_bot import *
from singsong_bot import *

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
          "要进入问候模式，请按G/g键\n"
          "To enter Chitchat mode, press the C/c key.\n"
          "要进入闲聊模式，请按C/c键\n"
          "To enter Singsong mode, press the S/s key.\n"
          "要进入歌唱家模式，请按S/s键\n"
          "To enter Professional mode, press the P/p key\n"
          "要进入专业模式，请按P/p键\n"
          "Furthermore, if you want to hear some gibberish, press the N/n key\n"
          "此外，想听点胡言乱语，请按N/n键\n"
          "Toad of truth, press the E/e key\n"
          "O-O，请按E/e键\n"
          "Type 'quit' to exit\n"
          "打出 'quit' 或“退出”来退出")

    # 获取键盘输入 Get keyboard input
    key = input()
    if key == 'G' or key == 'g':
        print("You are now in greeting mode.\n"
              "您已进入问候模式。\n"
              "In greeting mode, I can have a simple conversation with you, including greetings, small talk, etc.\n"
              "在问候模式下，我可以和你进行简单的对话，包括问候、寒喧等等。")
        chatbot_G.converse()

    elif key == 'C' or key == 'c':
        print("You are now in chitchat mode.\n"
              "您已进入闲聊模式。\n"
              "In chitchat mode, I can talk to you about interesting topics, such as telling jokes, stories, etc.\n"
              "在闲聊模式下，我可以和你聊点有趣的话题，比方说讲笑话、讲故事、等等。")
        chatbot_C.converse()

    elif key == 'P' or key == 'p':
        print("You are now in professional mode.\n"
              "您已进入专业模式。\n"
              "In professional mode, I can answer your questions about computer terminology, \n"
              "recite the periodic table, calculate pi, and more.\n"
              "在专业模式下，我可以为你解答有关计算机专业名词的问题，背诵元素周期表，计算圆周率（pi）等等。")
        chatbot_P.converse()

    elif key == 'N' or key == 'n':
        print("You are now in nonsense mode.\n"
              "您已进入胡言乱语模式。\n"
              "Mi vdfgdfhtf zrhc, n sgs awcefcz s zwzsf rgzSAFs gz zsdfz zsdf zs yui,otuyftd sevabb.\n"
              "瞹澀奪祓瀔鹖佶，筐囖蓻釁湹悑腝玟。")
        chatbot_N.converse()

    elif key == 'S' or key == 's':
        print("You are now in singsong mode.\n"
              "您已进入歌唱家模式。\n"
              "In singsong mode, you can click on a favorite song and I will sing it for you.\n"
              "在歌唱家模式下，你可以点一首喜爱的歌曲，我会唱给你听。")
        chatbot_S.converse()

    elif key == 'E' or key == 'e':
        print("You've entered ELDER care mode.\n"
              "您已进入长者关怀模式。\n"
              "O-O O-O O-O O-O\n"
              " =   =   =   = ")

    else:
        print("Sorry, please try again.\n"
              "抱歉，请再尝试一次。")


if __name__ == "__main__":
    chatbot_start()
