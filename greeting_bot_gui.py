"""
greeting_bot.py
问候模式的聊天机器人实现 Chatbot implementation in greeting mode
使用图形用户接口 Using the Graphical User Interface
作者：李 奕辰 Author: Yichen Li
"""
from PyQt5 import QtGui

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

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
    # 5、戴夫问好
    [
        s_dave,
        ["歪比巴布，ruarourou"]
    ],
    # 6、退出操作
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        s_quit,
        ["再见，保重。", "回见。"]
    ],
    # 7、其它输入
    [
        r"(.*)",
        ["I'm not sure I understand what you mean. Can you rephrase that?\n"
         "我不太明白你的意思。你能重新表述一下吗？"]
    ],
]

# Create a greeting chatbot instance 问候模式聊天机器人实例
chatbot_G = Chat(pairs_greeting, reflections)


class ChatbotApp(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(Greeting Mode)")
        self.setGeometry(100, 100, 400, 300)
        # self.setFont()
        # self.font().Bold()
        self.layout = QVBoxLayout()
        self.setFont(font)
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setText(
            "In greeting mode, I can have a simple conversation with you, including greetings, small talk, etc.\n"
            "在问候模式下，我可以和你进行简单的对话，包括问候、寒喧等等。\n")
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
            response = chatbot_G.respond(user_input)
            self.chat_area.append("Greeting Bot （问候模式聊天机器人）: " + response)
            self.input_area.clear()


# if __name__ == "__main__":
def greeting_bot_start():
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec_())
