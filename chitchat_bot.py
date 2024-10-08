"""
chitchat_bot.py
闲聊模式的聊天机器人实现 Chatbot implementation in chitchat mode
作者：李 奕辰 Author: Yichen Li
"""


# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections

# Chitchat Mode 闲聊模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_chitchat = [
    # 1、讲笑话
    [
        r"(.*)tell(.*)joke(.*)",
        ["Why did the scarecrow win an award?\n" 
         "Because he was outstanding in his field!"]
    ],
    [
        "(.*)" + s_tell + "(.*)" + s_joke + "(.*)",
        ["有一天，小明跟小华说：“我最近开始学游泳了！\n"
         "小华惊讶地问：“那你会不会淹水？\n"
         "小明自信地回答：“不会！我只在岸上练习！"]
    ]
]

# Create a chitchat chatbot instance 闲聊模式聊天机器人实例
chatbot_C = Chat(pairs_chitchat, reflections)

