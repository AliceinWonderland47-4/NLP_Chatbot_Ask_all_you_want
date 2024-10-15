"""
news_bot_gui.py
新闻模式的聊天机器人实现 Chatbot implementation in news mode
使用图形用户接口 Using the Graphical User Interface
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from nltk.chat.util import Chat, reflections
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QApplication
from PyQt5 import QtGui

# News Mode 新闻模式
# Define some pairs of input patterns and responses 定义一些输入问答对
# 国内新闻 Domestic News
pairs_news_dom = [
    [
        "2024/04/01",
        ["4月1日，国家重点能源项目——青海玛尔挡水电站正式发电。玛尔挡水电站位于青海果洛藏族自治州玛沁县拉加镇，\n"
         "总装机容量232万千瓦，是黄河流域海拔最高、在建装机容量最大的水电站。\n"
         "On April 1, the national key energy project, the Qinghai Maerdang Hydropower Station,\n"
         "officially started generating electricity. The Maerdang Hydropower Station is located\n"
         "in Lajia Town, Maqin County, Golog Tibetan Autonomous Prefecture, Qinghai Province.\n"
         "With a total installed capacity of 2.32 million kilowatts, it is the highest-altitude\n"
         "hydropower station in the Yellow River Basin and the largest hydropower station under construction."]
    ]
]

# 国际新闻
pairs_news_int = [
    [
        "2024/04/01",
        ["4月1日下午，国家主席习近平在北京人民大会堂同印尼当选总统普拉博沃举行会谈。中印尼关系取得宝贵成就，\n"
         "关键在于坚持战略自主、坚持互信互助、坚持合作共赢、坚持公平正义。\n"
         "On the afternoon of April 1, President Xi Jinping held talks with Indonesian\n"
         "President-elect Prabowo Subianto at the Great Hall of the People in Beijing.\n"
         "The key to the valuable achievements in China-Indonesia relations lies in\n"
         "adhering to strategic autonomy, mutual trust and mutual assistance, win-win\n"
         "cooperation, and fairness and justice."]
    ]
]

chatbot_Nd = Chat(pairs_news_dom, reflections)
chatbot_Ni = Chat(pairs_news_int, reflections)


# 国内新闻
class ChatbotApp_D(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(Domestic News)")
        self.setGeometry(100, 100, 400, 300)
        # self.setFont()
        # self.font().Bold()
        self.layout = QVBoxLayout()
        self.setFont(font)
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setText(
            "I provide you with the latest domestic current affairs news.\n"
            "Just enter the date (format: YYYY/MM/DD) to search.\n"
            "我为您提供最新的国内时事新闻，输入日期（格式：YYYY/MM/DD）即可查询。\n")
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
            response = chatbot_Nd.respond(user_input)
            self.chat_area.append("Bot （国内新闻聊天机器人）: " + response)
            self.input_area.clear()


class ChatbotApp_I(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(Domestic News)")
        self.setGeometry(100, 100, 400, 300)
        # self.setFont()
        # self.font().Bold()
        self.layout = QVBoxLayout()
        self.setFont(font)
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setText(
            "In chitchat mode, I can talk to you about interesting topics, such as telling jokes, stories, etc.\n"
            "在闲聊模式下，我可以和你聊点有趣的话题，比方说讲笑话、讲故事、等等。\n")
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
            response = chatbot_Ni.respond(user_input)
            self.chat_area.append("Chitchat Bot （闲聊模式聊天机器人）: " + response)
            self.input_area.clear()


def dom_news_bot_start():
    app = QApplication(sys.argv)
    window = ChatbotApp_D()
    window.show()
    sys.exit(app.exec_())


def int_news_bot_start():
    app = QApplication(sys.argv)
    window = ChatbotApp_I()
    window.show()
    sys.exit(app.exec_())

