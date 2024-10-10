------ EE 6405 自然语言处理 Natural Language Processing ------

------ 最终小组合作项目 Final group project B17 ------
------ 小组成员 Panelists A-Z ------


------ “有问必答”AI聊天机器人 AI chatbot that answers all your questions ------


------ 主要实现原理 Main implementation principle ------


------ 项目文件结构 Project file structure ------

Final_Project/ 根目录 Root Directory
---- corpus/ 语料库存放目录 Corpus storage directory
-------- user_dict/ 用户词典存放目录 User dictionary storage directory
------------ __init__.py
------------ sogou_dict1.txt
文件说明 File Description
处理好的（最终）词典文件，包含以下几种词性：The processed (final) dictionary file contains the following parts of speech:
1、sgjsj 搜狗计算机 专业计算机科学名词 Professional computer science terms （共10300个 A total of 10300）
2、kc 课程 大学计算机常见课程 Common University Computer Courses （共19个 A total of 19）
3、rm 人名 常见英文人名 Common English names （共36个 A total of 36）
4、
------------ test_user_dict.txt
文件说明 File Description
项目早期用于测试的用户词典 User dictionary for testing in the early stages of the project
------------ user_dict.txt
文件说明 File Description
处理前的用户词典 User dictionary before processing
-------- __init__.py
---- lib/ 存放基本方法，比如分词、停用词获取等 Store basic methods, such as word segmentation, stop word acquisition, etc.
-------- __init__.py
-------- cut_sentence.py
文件说明 File Description
分词功能的api实现，多种分词方法 API implementation of word segmentation function, multiple word segmentation methods

---- chat_api.py 聊天机器人程序主入口。Chatbot program main entrance

------------ 运行说明 ------------
1、config.py中的文件路径需要根据环境进行更改。The file paths in config.py need to be changed according to your environment.
2、
