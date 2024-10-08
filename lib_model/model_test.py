import fastText
import config

"""
构建模型
"""


def build_classify_model():
    # 输入数据中只包含一个词语
    model = fastText.train_supervised(config.classify_corpus_path, wordNgrams=1, epoch=20, minCount=5)
    model.save_model()


"""
加载模型
"""


def get_classify_model():
    pass


build_classify_model()
