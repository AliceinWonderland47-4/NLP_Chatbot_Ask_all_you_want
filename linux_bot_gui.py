"""
linux_bot_gui.py
Linux命令查询模式的聊天机器人实现 Chatbot implementation in Linux command query mode
使用图形用户接口 Using the Graphical User Interface
作者：李 奕辰 Author: Yichen Li
"""
from PyQt5 import QtGui

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

# Linux query Mode Linux命令查询模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_linux = [
    # 1、ab
    [
        r"(.*)ab(.*)",
        [
            "ab命令的作用是：ab命令是一个测试你Apache http服务器的工具，你可以通过这个工具，\n"
            "指定一个单位时间内向Apache发出的请求数量来看看你的Apache和机器配合的性能如何。\n"
            "The ab command is a tool for testing your Apache http server.\n"
            "You can use this tool to specify the number of requests sent to\n"
            "Apache per unit time to see how well your Apache and machine perform together."
        ]
    ],
    # 2、df
    [
        r"(.*)df(.*)",
        [
            "df命令的作用是：df命令用于显示磁盘分区上的可使用的磁盘空间。默认显示单位为KB。\n"
            "可以利用该命令来获取硬盘被占用了多少空间，目前还剩下多少空间等信息。\n"
            "The df command is used to display the available disk space\n"
            "on the disk partition. The default display unit is KB. You can use\n"
            "this command to obtain information such as how much space is occupied\n"
            "on the hard disk and how much space is currently left."
        ]
    ],
    # 3、date

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
chatbot_L = Chat(pairs_linux, reflections)


class ChatbotApp(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(Linux Mode)")
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
            response = chatbot_L.respond(user_input)
            self.chat_area.append("Linux Bot （Linux命令查询模式聊天机器人）: \n" + response)
            self.input_area.clear()


# if __name__ == "__main__":
def linux_bot_start():
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec_())
