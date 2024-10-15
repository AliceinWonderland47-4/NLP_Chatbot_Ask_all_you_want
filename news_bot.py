"""
news_bot.py
新闻模式的聊天机器人实现 Chatbot implementation in news mode
作者：李 奕辰 Author: Yichen Li
"""

# 导入相关模块 Import related modules
from nltk.chat.util import Chat, reflections

# News Mode 新闻模式
# Define some pairs of input patterns and responses 定义一些输入问答对
# 国内新闻 Domestic News
pairs_news_dom = [
    [
        "2024/4/1",
        ["4月1日，国家重点能源项目——青海玛尔挡水电站正式发电。玛尔挡水电站位于青海果洛藏族自治州玛沁县拉加镇，\n"
         "总装机容量232万千瓦，是黄河流域海拔最高、在建装机容量最大的水电站。\n"
         "On April 1, the national key energy project, the Qinghai Maerdang Hydropower Station,\n"
         "officially started generating electricity. The Maerdang Hydropower Station is located\n"
         "in Lajia Town, Maqin County, Golog Tibetan Autonomous Prefecture, Qinghai Province.\n"
         "With a total installed capacity of 2.32 million kilowatts, it is the highest-altitude\n"
         "hydropower station in the Yellow River Basin and the largest hydropower station under construction."]
    ]
]

pairs_news_int = [
    [
        "2024/4/1",
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
