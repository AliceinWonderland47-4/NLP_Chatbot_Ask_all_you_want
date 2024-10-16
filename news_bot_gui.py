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
        "2024/03/03",
        ["2024年3月3日，2024跳水世界杯蒙特利尔站比赛在加拿大蒙特利尔奥林匹克中心游泳馆落幕。\n"
         "中国跳水‘梦之队’包揽全部金牌，以9金、1银、2铜的成绩位列奖牌榜第一。\n"
         ""]
    ],
    [
        "2024/04/01",
        ["4月1日，国家重点能源项目——青海玛尔挡水电站正式发电。玛尔挡水电站位于青海果洛藏族自治州玛沁县拉加镇，\n"
         "总装机容量232万千瓦，是黄河流域海拔最高、在建装机容量最大的水电站。\n"
         "On April 1, the national key energy project, the Qinghai Maerdang Hydropower Station,\n"
         "officially started generating electricity. The Maerdang Hydropower Station is located\n"
         "in Lajia Town, Maqin County, Golog Tibetan Autonomous Prefecture, Qinghai Province.\n"
         "With a total installed capacity of 2.32 million kilowatts, it is the highest-altitude\n"
         "hydropower station in the Yellow River Basin and the largest hydropower station under construction."]
    ],
    [
        "2024/04/09",
        [
            "4月9日，由中国科学院深圳先进技术研究院和广州能源研究所共同主办的新型波浪能海洋生态监测浮标\n"
            "‘合作者号’启用仪式在深圳举行，我国自主研发的波浪能海洋生态监测浮标研发测试平台正式投入使用。\n"
            "On April 9, the launching ceremony of the new wave energy marine ecological monitoring buoy \n"
            "‘Cooperator’, co-organized by the Shenzhen Institutes of Advanced Technology of the Chinese Academy of \n"
            "Sciences and the Guangzhou Institute of Energy Conversion, was held in Shenzhen. my country’s \n"
            "independently developed wave energy marine ecological monitoring buoy R&D and testing platform was \n"
            "officially put into use. "
        ]
    ]
]

# 国际新闻 International News
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
    ],
    [
        "2024/04/06",
        ["俄罗斯‘联盟MS-24’载人飞船搭载3名宇航员从国际空间站返回地球，4月6日在哈萨克斯坦境内草原上安全着陆。\n"
         "Russia's Soyuz MS-24 manned spacecraft carrying three astronauts returned to\n"
         "Earth from the International Space Station and landed safely on the grasslands\n"
         "in Kazakhstan on April 6."]
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
            "我为您提供最新的国内时事新闻，输入日期（格式：YYYY/MM/DD）即可查询。\n"
            "Example: Enter 2024/04/01 in the blank box below and click the 'Send' button.\n"
            "使用示例：在下方的空白框中输入2024/04/01，然后点击‘发送’按钮。")
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
            self.chat_area.append("Bot （国内新闻聊天机器人）: \n" + response)
            self.input_area.clear()


# 国际新闻
class ChatbotApp_I(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(International News)")
        self.setGeometry(100, 100, 400, 300)
        # self.setFont()
        # self.font().Bold()
        self.layout = QVBoxLayout()
        self.setFont(font)
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setText(
            "I provide you with the latest international current affairs news.\n"
            "Just enter the date (format: YYYY/MM/DD) to search.\n"
            "我为您提供最新的国际时事新闻，输入日期（格式：YYYY/MM/DD）即可查询。\n"
            "Example: Enter 2024/04/01 in the blank box below and click the 'Send' button.\n"
            "使用示例：在下方的空白框中输入2024/04/01，然后点击‘发送’按钮。\n")
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
            self.chat_area.append("News Bot （国际新闻模式聊天机器人）: \n" + response)
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

