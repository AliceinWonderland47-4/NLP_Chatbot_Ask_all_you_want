"""
nonsense_bot.py
胡言乱语模式的聊天机器人实现 Chatbot implementation in nonsense mode
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from nltk.chat.util import Chat, reflections

# Nonsense Mode 胡言乱语模式
# Define some pairs of input patterns and responses 定义一些输入问答对
# Return Chinese/English garbled characters 返回中/英文乱码

pairs_nonsense = [
    [
        r"([\u4e00-\u9fff]+)",
        ["鲻齵暐，霓畀皟鋱骽？岙譬龢巭萜耆鳚。麂，禳砼吖蓲。\n"
         "辔錒霜，荻氟衮獲怚？褲囖駔孈膬鵯腝。幙，礐媉鉺鄏。"]
    ],
    [
        r"(^[a-zA-Z]+$)",
        ["sAfrgj, icv it awe ohgc razhjk. artyu---vuvnm, zdghgk izdxfg ccfh.\n"
         "Shkjgh? rcuyv vc ugjf, zfd2agf, chf kugjh huhu. Erdhyjg lhhlij b.\n"
         "Www jhtfk bhvgc o p;olkjhg xgju, zxgfhn ukuhku xtrg. hxgfcnhg zwzHG."]
    ]
]

# Create a nonsense chatbot instance 胡言乱语模式聊天机器人实例
chatbot_N = Chat(pairs_nonsense, reflections)
