"""
chat_api.py
聊天功能的接口 Chat interface
程序运行和测试入口 Program running and test entry
作者：李 奕辰 Author: Yichen Li
"""

import random

# 导入相关模块 Import related modules
# NLTK自然语言处理库 NLTK Natural Language Processing Library
import nltk

# 7种功能模式 7 function modes

# 1、问候模式 Greeting Mode
from greeting_bot import *
from greeting_bot_gui import *

# 2、闲聊模式 Chitchat Mode
from chitchat_bot import *
from chitchat_bot_gui import *

# 3、专业模式
from professional_bot import *
from professional_bot_gui import *

# 4、胡言乱语模式
from nonsense_bot import *

# 5、歌唱家模式
from singsong_bot import *
from singsong_bot_gui import *

# 6、长者模式
from elderly_bot import *

# 7、新闻模式
from news_bot import *
from news_bot_gui import *

# 字典
from dic_1 import *

# Download the punkt tokenizer if you haven't already
nltk.download('punkt')


# Start the conversation 开始对话
# The prompt words are bilingual, English on top and Chinese on the bottom 提示词为双语，英文在上，中文在下
def chatbot_start():
    print("Hello, I am the Ask and Answer chat robot, and I am happy to serve you.\n"
          "你好，我是“有问必答”聊天机器人，很高兴为你服务。\n"
          "What do you want to do today?\n"
          "今天想做些什么呢？\n"
          "1. To enter 'Greeting' mode, press the G/g key.\n"
          "1. 要进入 问候模式，请按G/g键\n"
          "2. To enter 'Chitchat' mode, press the C/c key.\n"
          "2. 要进入 闲聊模式，请按C/c键\n"
          "3. To enter 'Singsong' mode, press the S/s key.\n"
          "3. 要进入 歌唱家模式，请按S/s键\n"
          "4. To enter 'Professional' mode, press the P/p key\n"
          "4. 要进入 专业模式，请按P/p键\n"
          "5. To enter 'Beijing Dialect' mode, press the B/b key\n"
          "5. 要进入 北京话模式，请按B/b键\n"
          "6. To enter the naming assistant mode, press the T/t key\n"
          "6. 要进入 起名助手模式，请按T/t键\n"
          "7. To enter the News Enquiries mode, press the W/w key\n"
          "7. 要进入 新闻查询模式，请按W/w键\n"
          "8. Furthermore, if you want to hear some gibberish, press the N/n key\n"
          "8. 此外，想听点胡言乱语，请按N/n键\n"
          "9. Toad of truth, press the E/e key\n"
          "9. O-O，请按E/e键\n"
          "Type 'quit' to exit\n"
          "打出 'quit' 或“退出”来退出")

    # 获取键盘输入 Get keyboard input
    key = input()
    if key == 'B' or key == 'b':
        print("You are now in Beijing dialect mode.\n"
              "您已进入北京话模式。\n"
              "In Beijing dialect mode, I can chat with you in Beijing dialect.\n"
              "在北京话模式下，我可以和你嘚不嘚不。")
        while True:
            s = str(input())
            if s == "quit":
                return 0
            else:
                print(s + "儿")

    elif key == 'T' or key == 't':
        print("You are now in greeting mode.\n"
              "您已进入起名助手模式。\n"
              "In the naming assistant mode, tell me your baby's surname and I will give you a name (3 characters).\n"
              "在起名助手模式下，告诉我您家宝宝的姓氏，我给您起名字（3字）。")
        while True:
            surname = str(input("请输入姓氏："))
            if surname == "quit":
                return 0
            else:
                i1 = random.randint(0, 30)
                i2 = random.randint(0, 30)
                print("宝宝姓名：")
                print(surname + dic_1[i1] + dic_2[i2])

    elif key == 'G' or key == 'g':
        print("You are now in greeting mode. Please pay attention to the pop-up window.\n"
              "您已进入问候模式。请留意弹出的窗口。\n")
        # chatbot_G.converse()  # 旧版本，纯终端输入/输出 Old version, pure terminal input/output
        greeting_bot_start()  # 新版本，增加了GUI New version, added GUI

    # W键：新闻查询模式 news query mode
    elif key == 'W' or key == 'w':
        print("You are now in news query mode.\n"
              "您已进入新闻查询模式。\n"
              "In news query mode, I can share with you some domestic\n"
              "and international hot news that are worth paying attention to.\n"
              "在新闻查询模式下，我可以和你分享一些值得关注的国内外热点新闻。\n"
              "To learn about domestic hot news, please press the D/d key.\n"
              "了解国内热点新闻，请按D/d键。\n"
              "To learn about international hot news, please press the I/i key.\n"
              "了解国际热点新闻，请按I/i键。")
        key = input()
        if key == 'D' or key == 'd':
            # chatbot_Nd.converse()  # 旧版本，纯终端输入/输出 Old version, pure terminal input/output
            print("请留意弹出的窗口。Please pay attention to the pop-up window.")
            dom_news_bot_start()  # 新版本，增加了GUI New version, added GUI
        elif key == 'I' or key == 'i':
            # chatbot_Ni.converse()  # 旧版本，纯终端输入/输出 Old version, pure terminal input/output
            print("请留意弹出的窗口。Please pay attention to the pop-up window.")
            int_news_bot_start()  # 新版本，增加了GUI New version, added GUI

    # C键：闲聊模式 chitchat mode
    elif key == 'C' or key == 'c':
        print("You are now in chitchat mode. Please pay attention to the pop-up window.\n"
              "您已进入闲聊模式。请留意弹出的窗口。\n")
        # chatbot_C.converse()  # 旧版本，纯终端输入/输出 Old version, pure terminal input/output
        chitchat_bot_start()  # 新版本，增加了GUI New version, added GUI

    # P键：专业模式 professional mode
    elif key == 'P' or key == 'p':
        print("You are now in professional mode. Please pay attention to the pop-up window.\n"
              "您已进入专业模式。请留意弹出的窗口。\n")
        # chatbot_P.converse()  # 旧版本，纯终端输入/输出 Old version, pure terminal input/output
        professional_bot_start()  # 新版本，增加了GUI New version, added GUI

    elif key == 'N' or key == 'n':
        print("You are now in nonsense mode.\n"
              "您已进入胡言乱语模式。\n"
              "Mi vdfgdfhtf zrhc, n sgs awcefcz s zwzsf rgzSAFs gz zsdfz zsdf zs yui,otuyftd sevabb.\n"
              "瞹澀奪祓瀔鹖佶，筐囖蓻釁湹悑腝玟。")
        chatbot_N.converse()

    # S键：歌唱家模式 singsong mode
    elif key == 'S' or key == 's':
        print("You are now in singsong mode. Please pay attention to the pop-up window.\n"
              "您已进入歌唱家模式。请留意弹出的窗口。\n")
        # chatbot_S.converse()  # 旧版本，纯终端输入/输出 Old version, pure terminal input/output
        singsong_bot_start()  # 新版本，增加了GUI New version, added GUI

    elif key == 'E' or key == 'e':
        print("You've entered ELDER care mode.\n"
              "您已进入长者关怀模式。\n"
              "O-O O-O O-O O-O\n"
              " =   =   =   = ")
        chatbot_E.converse()

    else:
        print("Sorry, please try again.\n"
              "抱歉，请再尝试一次。")


if __name__ == "__main__":
    chatbot_start()
