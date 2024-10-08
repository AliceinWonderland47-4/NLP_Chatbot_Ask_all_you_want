"""
greeting_bot.py
问候模式的聊天机器人实现 Chatbot implementation in greeting mode
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections


# Greeting Mode 问候模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_greeting = [
    # 1、用户（“我”）的名字
    [
        r"(.*) [Mm]y [Nn]ame [Ii]s_name (.*)",  # 适配短语my name is（我的名字是）
        ["Hello, how can I assist you today?"]
    ],
    [
        "(.*)" + s_my + s_name + "(.*)",  # 适配短语my name is（我的名字是）
        ["您好，今天我可以为您提供什么帮助？"]
    ],
    # 2、你好
    [
        r"[Hh]i|[Hh]ello|[Hh]ey(.*)",  # 适配单词Hi, Hello, Hey
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        s_hello + "(.*)",  # 适配单词Hi, Hello, Hey
        ["你好。", "别来无恙。", "嘿！我能帮你什么忙吗？"]
    ],
    # 3、（你）怎么样
    [
        r"(.*)[Hh]ow [Aa]re [Yy]ou(.*)?",  # 提取'how are you'（你怎么样），适配大小写习惯
        ["I'm just a bunch of code, but thanks for asking!\n"
         "我只是一堆代码，但还是感谢您的询问！",
         "Doing well, how about you?\n"
         "还好吧，你呢？"]
    ],
    [
        r"(.*)[Hh]ow [Aa]re [Yy]ou(.*)?",  # 提取'how are you'（你怎么样），适配大小写习惯
        ["I'm just a bunch of code, but thanks for asking!\n"
         "我只是一堆代码，但还是感谢您的询问！",
         "Doing well, how about you?\n"
         "还好吧，你呢？"]
    ],
    # 4、用户询问chatbot名字
    [
        r"(.*)[Yy]our [Nn]ame(.*)",  # 提取词组 your name（你的名字）
        ["I am a chatbot created using NLTK!\n"]
    ],
    # TODO: 中文输入的问题？
    [
        "(.*)" + s_you + "(.*)" + s_name + "(.*)",
        ["我是使用 NLTK 创建的聊天机器人。"]
    ],
    # 5、退出操作
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        s_quit,
        ["再见，保重。", "回见。"]
    ],
    # 6、其它输入
    [
        r"(.*)",
        ["I'm not sure I understand what you mean. Can you rephrase that?\n"
         "我不太明白你的意思。你能重新表述一下吗？"]
    ],
]

# Create a greeting chatbot instance 问候模式聊天机器人实例
chatbot_G = Chat(pairs_greeting, reflections)
