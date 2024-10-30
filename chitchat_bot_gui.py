"""
chitchat_bot_gui.py
闲聊模式的聊天机器人实现 Chatbot implementation in chitchat mode
使用图形用户接口 Using the Graphical User Interface
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QApplication
from PyQt5 import QtGui

# Chitchat Mode 闲聊模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_chitchat = [
    # 1、讲笑话 Tell jokes
    [
        r"(.*)[Tt]ell(.*)[Jj]oke(.*)",
        ["Why did the scarecrow win an award?\n"
         "Because he was outstanding in his field!"]
    ],
    [
        "(.*)" + s_tell + "(.*)" + s_joke + "(.*)",
        ["有一天，小明跟小华说：“我最近开始学游泳了！”\n"
         "小华惊讶地问：“那你会不会淹水？”\n"
         "小明自信地回答：“不会！我只在岸上练习！”"]
    ],
    # 2、讲故事（有趣的故事）Telling stories (interesting stories)
    [
        r"(.*)interesting story(.*)",
        ["In a small town, there was an old clock tower\n"
         "that had stopped at exactly 3:15 for decades.\n"
         "Legend had it that if someone could get the clock\n"
         "to tick again, they would be granted a wish.\n"
         "One rainy evening, a curious girl named Mia decided\n"
         "to climb the tower. She carefully opened the creaky door\n"
         "and found the dusty gears inside. Remembering her\n"
         "grandmother’s tales, she whispered her wish: “I wish for a friend.”\n"
         "To her surprise, the clock began to tick! As the hands moved,\n"
         "a warm light filled the room, and before her stood a small,\n"
         "mischievous fox with bright eyes.\n"
         "“Let’s go!” the fox said with a grin. From that day on,\n"
         "Mia and her magical friend explored the town together,\n"
         "uncovering hidden secrets and sharing countless adventures,\n"
         "proving that wishes can lead to the most unexpected friendships."]
    ],
    [
        "(.*)" + s_interesting + s_story + "(.*)",
        ["在一个小镇上，有一座古老的钟楼，几十年来一直停在 3:15 的正点。\n"
         "传说如果有人能让钟再次滴答作响，他们就能实现一个愿望。\n"
         "一个下雨的晚上，一个名叫米娅的好奇女孩决定爬上塔楼。她小心翼翼地\n"
         "打开吱吱作响的门，发现里面布满灰尘的齿轮。想起祖母的故事，她低声说出了自己的愿望：\n"
         "“我希望有一个朋友。”\n"
         "令她惊讶的是，时钟开始滴答作响！随着指针的移动，一束温暖的光线充满了房间，\n"
         "她面前站着一只眼睛明亮的小淘气狐狸。\n"
         "“我们走吧！”狐狸笑着说。从那天起，米娅和她神奇的朋友一起探索小镇，\n"
         "揭开隐藏的秘密，分享无数冒险，证明了愿望可以带来最意想不到的友谊。"]
    ],
    # 3、讲故事（恐怖的故事）Telling stories (horrifying stories)
    [
        r"(.*)horrifying story(.*)",
        ["Late one night, Sarah received a message from her friend Lily:\n"
         "“I’m in trouble. Please help me.” Worried, she rushed to Lily’s house,\n"
         "but as she approached, something felt off. The lights were off,\n"
         "and the front door stood ajar.\n"
         "Inside, silence enveloped her. “Lily?” she called, but only her echo replied.\n"
         "Heart racing, Sarah crept through the darkened rooms,\n"
         "her phone flashlight flickering. In the living room,\n"
         "she found a note on the coffee table, scrawled in shaky handwriting:\n"
         "“Don’t trust anyone. It’s already inside.”\n"
         "Suddenly, a cold breeze swept through the room, extinguishing her light.\n"
         "Panic surged as Sarah turned to flee, but the door slammed shut.\n"
         "In the darkness, she heard a soft whisper behind her: “You shouldn’t have come.”\n"
         "With no way out, Sarah felt a chilling hand grasp her shoulder."]
    ],
    [
        "(.*)" + s_scary + s_story + "(.*)",
        ["一天深夜，莎拉收到了朋友莉莉发来的消息：“我有麻烦了。请帮帮我。”\n"
         "她焦急万分，赶到莉莉家，但走近时，她感觉到有些不对劲。灯灭了，前门半开着。\n"
         "屋内一片寂静。“莉莉？”她叫道，但只有回声回应。\n"
         "莎拉心跳加速，蹑手蹑脚地穿过黑暗的房间，手机手电筒闪烁不定。\n"
         "在客厅里，她在咖啡桌上发现了一张纸条，上面用颤抖的笔迹潦草地写着：\n"
         "“不要相信任何人。它已经在里面了。”\n"
         "突然，一股冷风吹过房间，熄灭了灯。莎拉惊慌失措，转身逃跑，但门却砰地关上了。\n"
         "在黑暗中，她听到身后传来一声轻声低语：“你不该来的。”\n"
         "无路可走的莎拉感到一只冰冷的手抓住了她的肩膀。"]
    ],
    [
        r"(.*)heartbroken(.*)comfort(.*)",
        [
            "Don't try to chase a missed horse. Use the time you spend\n"
            "chasing the horse to plant grass. The horse will come naturally\n"
            "when the spring comes. The same principle applies to a broken heart."
        ]
    ],
    [
        "(.*)" + s_heart + "(.*)" + s_comf + "(.*)",
        [
            "不要试图去追一匹错过的马，用追马的时间去种草，来年春暖花开，骏马自然会来。同样的道理，也适用于失恋。"
        ]
    ],
    [
        "(.*)" + s_beau + "(.*)" + s_sentence + "(.*)",
        [
            "听一场雨，雨碎江南；看一场雪，雪漫西山；吹一场风，风吹河畔；\n"
            "误一场缘，缘尽情散；唱一场戏，戏落泪干；醉一场酒，酒醒夜寒。"
        ]
    ],
    [
        r"(.*)beautiful sentence(.*)",
        [
            "Listen to a rain, the rain shatters the south of the Yangtze River;\n"
            "watch a snow, the snow covers the western mountains; blow a wind, \n"
            "the wind blows by the river; miss a fate, the fate is gone; sing a play,\n"
            "the tears dry; get drunk, the night is cold when you wake up."
        ]
    ],

    # 退出操作 Exit Operation
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        s_quit,
        ["再见，保重。", "回见。"]
    ],
    # 其它输入 Other inputs
    [
        r"(.*)",
        ["I'm not sure I understand what you mean. Can you rephrase that?\n"
         "我不太明白你的意思。你能重新表述一下吗？"]
    ],
]

# Create a chitchat chatbot instance 闲聊模式聊天机器人实例
chatbot_C = Chat(pairs_chitchat, reflections)


class ChatbotApp(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(Chitchat Mode)")
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
            response = chatbot_C.respond(user_input)
            self.chat_area.append("Chitchat Bot （闲聊模式聊天机器人）: \n" + response)
            self.input_area.clear()


# if __name__ == "__main__":
def chitchat_bot_start():
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec_())
