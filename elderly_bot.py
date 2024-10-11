"""
elderly_bot.py
长者模式的聊天机器人实现 Chatbot implementation in elderly mode
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections
from elder_trans_pairs import *

# Elderly Mode 长者模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_elderly = [
    [
        s_hk_jour,
        ["你们啊，比那些西方记者跑得还快"]
    ],
    [
        s_suc,
        ["连任，连任也是按照基本法，按照选举的法去产生"]
    ],
    [
        s_dong,
        ["董先生现在是当特首——我们怎么能不支持特首啊"]
    ],
    [
        s_sup,
        ["兹磁啊，资瓷"]
    ],
    [
        s_wallace,
        ["比你们强到不知哪里去了，我跟他谈笑风生"]
    ]
]

# Create an elderly chatbot instance 长者模式聊天机器人实例
chatbot_E = Chat(pairs_elderly, reflections)
