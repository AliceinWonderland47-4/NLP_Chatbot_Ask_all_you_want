"""
professional_bot.py
专业模式的聊天机器人实现 Chatbot implementation in professional mode
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections
from professional_trans_pairs import *

# Professional Mode 专业模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_professional = [
    [
        r"(.*)Amdahl's Law(.*)",
        ["In computer architecture, Amdahl's law (or Amdahl's argument)\n"
         "is a formula which gives the theoretical speedup in latency of\n"
         "the execution of a task at fixed workload that can be expected\n"
         "of a system whose resources are improved.\n"
         "The law can be stated as:\n"
         "the overall performance improvement gained by optimizing a single\n"
         "part of a system is limited by the fraction of time that the improved\n"
         "part is actually used"]
    ],
    [
        "(.*)" + s_Amdahl + "(.*)",
        [
            "在计算机架构中，阿姆达尔定律（或阿姆达尔论证）\n"
            "是一个公式，它给出了在固定工作负载下执行任务时，\n"
            "资源得到改善的系统在理论上可以实现的延迟加速。\n"
            "该定律可以表述为：\n"
            "通过优化系统的单个部分所获得的整体性能改进，\n"
            "受限于实际使用改进部分的时间比例。"
        ]
    ]
]

# Create a professional chatbot instance 专业模式聊天机器人实例
chatbot_P = Chat(pairs_professional, reflections)
