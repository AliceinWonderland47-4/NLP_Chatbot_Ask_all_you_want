"""
professional_bot_gui.py
专业模式的聊天机器人实现 Chatbot implementation in professional mode
使用图形用户接口 Using the Graphical User Interface
作者：李 奕辰 Author: Yichen Li
"""
import sys

# 导入相关模块 Import related modules
from common_trans_pairs import *
from nltk.chat.util import Chat, reflections
from professional_trans_pairs import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

# Professional Mode 专业模式
# Define some pairs of input patterns and responses 定义一些输入问答对
pairs_professional = [
    # 1、A-阿姆达尔定律（Amdahl's Law）
    [
        r"(.*)[Aa]mdahl's [Ll]aw(.*)",
        ["In computer architecture, Amdahl's law (or Amdahl's argument)\n"
         "is a formula which gives the theoretical speedup in latency of\n"
         "the execution of a task at fixed workload that can be expected\n"
         "of a system whose resources are improved.\n"
         "The law can be stated as:\n"
         "the overall performance improvement gained by optimizing a single\n"
         "part of a system is limited by the fraction of time that the improved\n"
         "part is actually used."]
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
    ],
    # 2、B-巴克斯范式（Backus Paradigm）
    [
        r"(.*)Backus Paradigm(.*)",
        ["Backus-Naur Form, or Backus Paradigm, is a language used to represent\n"
         "context-free grammars, which describe a class of\n"
         "formal languages. It was first introduced by John\n"
         "Backus and Peter Naur to describe the syntax of\n"
         "computer languages."]
    ],
    [
        "(.*)" + s_Backus + "(.*)",
        ["巴克斯范式，是一种用于表示上下文无关文法的语言，上下文无关文法\n"
         "描述了一类形式语言。它是由约翰·巴科斯（John Backus）和彼得·诺尔（Peter Naur）\n"
         "首先引入的用来描述计算机语言语法的符号集。"]
    ],
    # 3、C-词法分析（Lexical Analysis）
    [
        r"(.*)Lexical Analysis(.*)",
        ["Lexical tokenization (Lexical Analysis) is conversion of a text into\n"
         "(semantically or syntactically) meaningful lexical tokens belonging to\n"
         "categories defined by a lexer program. In case of a natural language,\n"
         "those categories include nouns, verbs, adjectives, punctuations etc.\n"
         "In case of a programming language, the categories include identifiers,\n"
         "operators, grouping symbols and data types."]
    ],
    [
        "(.*)" + s_Lexical + "(.*)",
        ["词汇标记化（词法分析）是将文本转换为（语义或句法上）有意义的词汇标记，这些词汇标记属于\n"
         "“词法分析器”程序定义的类别。对于自然语言，这些类别包括名词、动词、形容词、标点符号等。\n"
         "对于编程语言，这些类别包括标识符、运算符、分组符号和数据类型。"]
    ],

    [
        "(.*)" + s_bas_ass + "(.*)",
        ["理性人假设\n"
         "信息完全假设\n"
         "市场出清假设"]
    ],
    [
        "(.*)" + s_re_t + "(.*)",
        ["亚当·斯密相关理论（看不见的手）\n"
         "亚里士多德相关理论（自然、非自然）\n"
         "绝对优势理论\n"
         "比较优势理论\n"
         "行为经济学\n"
         "福利经济学\n"
         "重商主义"]
    ],
    [
        "(.*)" + s_manag + "(.*)" + s_con + "(.*)",
        ["管理是指组织中的管理者，通过实施计划、组织、人员配备、领导、控制等职能来协调他人的活动，"
         "使他人同自己一起实现既定目标的活动过程。"]
    ],
    [
        "(.*)" + s_manag + "(.*)" + s_fun + "(.*)",
        ["管理的职能包括：计划（核心环节）、组织、领导、控制。"]
    ],
    [
        "(.*)" + s_manag + "(.*)" + s_char + "(.*)",
        ["管理的特性包括：二重性、科学性、艺术性。"]
    ],
    [
        "(.*)" + s_manag + s_theo + "(.*)",
        ["主要的管理理论包括：\n"
         "科学管理理论\n"
         "法约尔的组织管理理论\n"
         "马克斯·韦伯的理想行政组织理论\n"
         "马斯洛的需求层次理论\n"
         "梅奥的霍桑试验，等等。"]
    ],
    [
        "(.*)" + s_dec + "(.*)" + s_con + "(.*)",
        ["决策是指，组织或个人为了实现某种目标而对未来一定时期内有关活动的方向、"
         "内容及方式的选择或调整过程。"]
    ],
    [
        "(.*)" + s_dec + "(.*)" + s_met + "(.*)",
        ["决策的方法包括：头脑风暴法、德尔菲法、哥顿法、名义群体法等。"]
    ],
    [
        "(.*)" + s_plan + "(.*)" + s_con + "(.*)",
        ["计划的概念是，根据组织内、外部的实际情况，权衡客观需要的主观可能，通过科学的预测，"
         "提出在一定未来时期内组织所要达到的目标以及实现目标的方法，是管理的首要职能。"]
    ],
    [
        "(.*)" + s_flex + "(.*)" + s_for + "(.*)",
        ["弹性的一般公式为：弹性系数 = 因变量的变动比例/自变量的变动比例"]
    ],
    [
        "(.*)" + s_req + "(.*)" + s_func + "(.*)",
        ["单个商品的需求函数：Qd = f(P)"]
    ],
    [
        "(.*)5W1H(.*)",
        ["(1) What————做什么？目标与内容；\n"
         "(2) Why————为什么做？原因；\n"
         "(3) Who————谁去做？目标与内容；\n"
         "(4) Where————何地做？地点；\n"
         "(5) When————何时做？时间；\n"
         "(6) How————怎样做？方式、手段。\n"]
    ],
    [
        "(.*)SMART(.*)",
        ["S: Specific，即明确性。代表目标必须是具体明确的。\n"
         "M: Measurable，即可衡量性。代表目标必须是可度量的。\n"
         "A: Attainable，即可实现性。代表目标必须是可实现的。\n"
         "R: Relevant，即相关性。代表目标必须和其他目标具有相关性。\n"
         "T: Time-based，即时效性。代表目标的达成必须有明确的时间限制（截止日期）。"]
    ],
    [
        "(.*)" + s_org + "(.*)" + s_str + "(.*)",
        ["组织结构主要包括以下几种：\n"
         "（1）直线型组织结构；\n"
         "（2）职能型组织结构；\n"
         "（3）直线-职能型组织结构；\n"
         "（4）事业部制组织结构；\n"
         "（5）矩阵型组织结构。"
         ]
    ],
    [
        "(.*)" + s_lead + "(.*)" + s_con + "(.*)",
        [
            "领导是指指挥、带领、引导和鼓励部下为实现目标而努力的过程。"
        ]
    ],
    [
        "(.*)" + s_lead + "(.*)" + s_use + "(.*)",
        [
            "领导的作用包括：指挥作用、协调作用和激励作用。"
        ]
    ],



    # 元素周期表 Periodic Table
    [
        r"(.*)[Pp]eriodic [Tt]able(.*)",
        ["Here’s the list of elements from 1 to 118:\n"
         "1. Hydrogen (H)\n"
         "2. Helium (He)\n"
         "3. Lithium (Li)\n"
         "4. Beryllium (Be)\n"
         "5. Boron (B)\n"
         "6. Carbon (C)\n"
         "7. Nitrogen (N)\n"
         "8. Oxygen (O)\n"
         "9. Fluorine (F)\n"
         "10. Neon (Ne)\n"
         "11. Sodium (Na)\n"
         "12. Magnesium (Mg)\n"
         "13. Aluminum (Al)\n"
         "14. Silicon (Si)\n"
         "15. Phosphorus (P)\n"
         "16. Sulfur (S)\n"
         "17. Chlorine (Cl)\n"
         "18. Argon (Ar)\n"
         "19. Potassium (K)\n"
         "20. Calcium (Ca)\n"
         "21. Scandium (Sc)\n"
         "22. Titanium (Ti)\n"
         "23. Vanadium (V)\n"
         "24. Chromium (Cr)\n"
         "25. Manganese (Mn)\n"
         "26. Iron (Fe)\n"
         "27. Cobalt (Co)\n"
         "28. Nickel (Ni)\n"
         "29. Copper (Cu)\n"
         "30. Zinc (Zn)\n"
         "31. Gallium (Ga)\n"
         "32. Germanium (Ge)\n"
         "33. Arsenic (As)\n"
         "34. Selenium (Se)\n"
         "35. Bromine (Br)\n"
         "36. Krypton (Kr)\n"
         "37. Rubidium (Rb)\n"
         "38. Strontium (Sr)\n"
         "39. Yttrium (Y)\n"
         "40. Zirconium (Zr)\n"
         "41. Niobium (Nb)\n"
         "42. Molybdenum (Mo)\n"
         "43. Technetium (Tc)\n"
         "44. Ruthenium (Ru)\n"
         "45. Rhodium (Rh)\n"
         "46. Palladium (Pd)\n"
         "47. Silver (Ag)\n"
         "48. Cadmium (Cd)\n"
         "49. Indium (In)\n"
         "50. Tin (Sn)\n"
         "51. Antimony (Sb)\n"
         "52. Tellurium (Te)\n"
         "53. Iodine (I)\n"
         "54. Xenon (Xe)\n"
         "55. Cesium (Cs)\n"
         "56. Barium (Ba)\n"
         "57. Lanthanum (La)\n"
         "58. Cerium (Ce)\n"
         "59. Praseodymium (Pr)\n"
         "60. Neodymium (Nd)\n"
         "61. Promethium (Pm)\n"
         "62. Samarium (Sm)\n"
         "63. Europium (Eu)\n"
         "64. Gadolinium (Gd)\n"
         "65. Terbium (Tb)\n"
         "66. Dysprosium (Dy)\n"
         "67. Holmium (Ho)\n"
         "68. Erbium (Er)\n"
         "69. Thulium (Tm)\n"
         "70. Ytterbium (Yb)\n"
         "71. Lutetium (Lu)\n"
         "72. Hafnium (Hf)\n"
         "73. Tantalum (Ta)\n"
         "74. Tungsten (W)\n"
         "75. Rhenium (Re)\n"
         "76. Osmium (Os)\n"
         "77. Iridium (Ir)\n"
         "78. Platinum (Pt)\n"
         "79. Gold (Au)\n"
         "80. Mercury (Hg)\n"
         "81. Thallium (Tl)\n"
         "82. Lead (Pb)\n"
         "83. Bismuth (Bi)\n"
         "84. Polonium (Po)\n"
         "85. Astatine (At)\n"
         "86. Radon (Rn)\n"
         "87. Francium (Fr)\n"
         "88. Radium (Ra)\n"]
    ],
    [
        "(.*)" + s_periodic + "(.*)",
        ["氢，氦，锂，铍，硼\n"
         "碳，氮，氧，氟，氖\n"
         "钠，镁，铝，硅，磷\n"
         "硫，氯，氩，钾，钙\n"
         "钪，钛，钒，铬，锰\n"
         "铁，钴，镍，铜，锌\n"
         "镓，锗，砷，硒，溴\n"
         "氪，铷，锶，钇，锆\n"
         "铌，钼，锝，钌，铑\n"
         "钯，银，镉，铟，锡\n"
         "锑，碲，碘，氙，铯\n"
         "钡，镧，钫，钽，钨\n"
         "铼，锇，铱，铂，金\n"
         "之类的"]
    ]
]

# Create a professional chatbot instance 专业模式聊天机器人实例
chatbot_P = Chat(pairs_professional, reflections)


class ChatbotApp(QWidget):
    def __init__(self):
        super().__init__()
        # 字体设置
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(18)  # 括号里的数字可以设置成自己想要的字体大小
        self.setWindowTitle("Chatbot(Professional Mode)")
        self.setGeometry(100, 100, 400, 300)
        # self.setFont()
        # self.font().Bold()
        self.layout = QVBoxLayout()
        self.setFont(font)
        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)
        self.chat_area.setText(
            "In professional mode, I can answer your questions about computer science and economics terminology, \n"
            "recite the periodic table, calculate pi, and more.\n"
            "在专业模式下，我可以为你解答有关计算机科学和经济学专业名词的问题，背诵元素周期表，计算圆周率（pi）等等。\n"
            "Type your question in the blank box below and click the 'Send' button.\n"
            "在下方的空白框内输入你的问题，然后点击‘发送’按钮。\n"
            "Example question in English: What is Amdahl's law?\n"
            "中文问题示例：管理的职能有哪些？")
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
            response = chatbot_P.respond(user_input)
            self.chat_area.append("Professional Bot （专业模式聊天机器人）: \n" + response)
            self.input_area.clear()


# if __name__ == "__main__":
def professional_bot_start():
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec_())
