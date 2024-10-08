"""
分词
"""
# 导入所需的包
import logging
import jieba
import jieba.posseg as psg
import config
import re
import string

# 加载词典
jieba.load_userdict(config.user_dict_path)

jieba.setLogLevel(logging.INFO)

letters = string.ascii_lowercase  # 小写字母
filters = [",", "-", ".", " "]  # 去除的标点
# 停用词
stopwords = set([i.strip() for i in open(config.stopwords_path, encoding='utf-8').readlines()])


def cut_word(sentence):
    """实现中英文分词"""
    # 对中文按字处理
    sentence = re.sub("\s+", " ", sentence)
    sentence = sentence.strip()
    result = []
    temp = ""
    for word in sentence:
        if word.lower() in letters:
            temp += word.lower()
        else:
            if temp != "":
                result.append(temp)
                temp = ""
            if word.strip() in filters:
                continue
            else:
                result.append(word)
    if temp != "":
        result.append(temp)
    return result


def cut(sentence, by_words=False, use_stopwords=False, with_sg=False):
    """
    :param sentence: 传入参数
    :param by_words: 是否按照单个字进行分词
    :param use_stopwords: 是否使用停用词
    :param with_sg: 是否返回词性
    :return:
    """
    assert by_words != True or with_sg != True, "根据word切分时无法返回词性"
    if by_words:
        return cut_word(sentence)
    else:
        ret = psg.lcut(sentence)

        if use_stopwords:
            ret = [(i.word, i.flag) for i in ret if i.word not in stopwords]
        if not with_sg:
            ret = [i.word for i in ret]

        return ret
