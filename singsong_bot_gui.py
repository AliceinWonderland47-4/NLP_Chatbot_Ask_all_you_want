"""
singsong_bot.py
歌唱家模式的聊天机器人实现 Chatbot implementation in singsong mode
使用图形用户接口 Using the Graphical User Interface
作者：李 奕辰 Author: Yichen Li
"""
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QApplication
from PyQt5 import QtGui

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
    # 5、《改革春风吹满地》
    [
        s_ggcf,
        ["人是衣，马是鞍/\n"
         "一看长相二看穿/\n"
         "白天想，夜里哭/\n"
         "做梦都想去首都/\n"
         "俩脚离地了/\n"
         "病毒就关闭了/\n"
         "啥都上不去了/\n"
         "嚎，嗷/\n"
         "改革春风吹满地/\n"
         "中国人民真争气/\n"
         "这个世界太疯狂/\n"
         "耗子都给猫当伴娘/\n"
         "齐德隆，齐东强，合一/\n"
         "齐德隆的咚的隆咚锵/"]
    ],
    # # 6、《》
    # []

]

# Create a singsong chatbot instance 歌唱家模式聊天机器人实例
chatbot_S = Chat(pairs_singsong, reflections)


class ChatbotApp(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(Singsong Mode)")
        self.setGeometry(100, 100, 400, 300)
        # self.setFont()
        # self.font().Bold()
        self.layout = QVBoxLayout()
        self.setFont(font)
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setText(
            "In singsong mode, you can click on a favorite song and I will sing it for you.\n"
            "在歌唱家模式下，你可以点一首喜爱的歌曲，我会唱给你听。\n")
        self.layout.addWidget(self.chat_area)

        self.input_area = QTextEdit(self)
        self.layout.addWidget(self.input_area)

        self.send_button = QPushButton("Send 发送", self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def send_message(self):
        user_input = self.input_area.toPlainText().strip()
        if user_input:
            self.chat_area.append("You （用户）: " + user_input)
            response = chatbot_S.respond(user_input)
            self.chat_area.append("Singsong Bot （歌唱家模式聊天机器人）: \n" + response)
            self.input_area.clear()


# if __name__ == "__main__":
def singsong_bot_start():
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec_())
