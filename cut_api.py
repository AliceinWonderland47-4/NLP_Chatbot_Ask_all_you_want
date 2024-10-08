"""
cut_api.py
语句分词功能接口 Sentence segmentation function interface
作者：李 奕辰 Author: Yichen Li
"""


from prepare_corpus.prepare_user_dict.test_user_dict import test_user_dict
from lib import cut_sentence

if __name__ == '__main__':
    # test_user_dict()
    # a = 'python和c++哪个难?UI和UE呢haha'
    # a = '我喜欢你，有机会吗？Can you do organic chemistry?'
    # a = '你好，我想学r语言，有什么教科书推荐吗？'
    # a = '你好，我想学自然语言处理，有什么教科书推荐吗？'
    a = '我是Steven, 想了解一下数据科学。'
    print(cut_sentence.cut(a))  # 分词方法1：简单按含义分词
    print(cut_sentence.cut(a, by_words=True))  # 分词方法2：单汉字/英文单词拆分
    print(cut_sentence.cut(a, by_words=False, use_stopwords=True, with_sg=True))  # 分词方法3：去除停用词，返回词性
    # print(cut_sentence.cut(a, by_words=False, use_stopwords=True, with_sg=False))  # 分词方法4：去除停用词，不返回词性
    print(cut_sentence.cut(a, by_words=False, use_stopwords=False, with_sg=True))  # 分词方法5：不去除停用词，返回词性
