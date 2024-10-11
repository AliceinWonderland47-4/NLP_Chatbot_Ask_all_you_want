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
    # 1、A-阿姆达尔定律（Amdahl's Law）
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
