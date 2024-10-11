"""
singsong_bot.py
歌唱家模式的聊天机器人实现 Chatbot implementation in singsong mode
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections
from professional_trans_pairs import *

# Singsong Mode 歌唱家模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_singsong = [
    # 1、《Staying Alive -- Bee Gees》
    [
        r"(.*)Staying Alive(.*)",
        ["Whether you're a brother or whether you're a mother/\n"
         "You're stayin' alive stayin' alive/\n"
         "Feel the city breakin' and everybody shakin'/\n"
         "And we're stayin' alive stayin' alive/\n"
         "Ah ha ha ha stayin' alive stayin' alive/\n"
         "Ah ha ha ha stayin' alive/"]
    ],
    # 2、《Style -- Taylor Swift -- 1989》
    [
        r"(.*)Style(.*)",
        ["You got that James Dean daydream look in your eye/\n"
         "And I got that red lip classic thing that you like/\n"
         "And when we go crashing down we come back every time/\n"
         "'Cause we never go out of style/\n"
         "We never go out of style/"]
    ],
    # 3、《I hate myself for loving you -- Joan Jett》
    [
        r"(.*)I [Hh]ate [Mm]yself [Ff]or [Ll]oving [Yy]ou(.*)",
        ["I think of you every night and day/\n"
         "You took my heart and you took my pride away/\n"
         "I hate myself for loving you/\n"
         "Can't break free from the things that you do/\n"
         "I wanna walk but I run back to you that's why/\n"
         "I hate myself for loving you/"]
    ],
    # 4、《Play that funky music -- Wild Cherry》
    [
        r"(.*)[Pp]lay [Tt]hat [Ff]unky [Mm]usic(.*)",
        ["When they were singin' and dancin' and movin' to the groovin'/\n"
         "And just when it hit me somebody turned around and shouted/\n"
         "Play that funky music white boy/\n"
         "Play that funky music right/"]
    ],
    # 5、《》

]

# Create a singsong chatbot instance 歌唱家模式聊天机器人实例
chatbot_S = Chat(pairs_singsong, reflections)
