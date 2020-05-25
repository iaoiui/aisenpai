from gensim.models.fasttext import FastText
import os


class fastTextWrapper():
    def __init__(self):
        self.sg_model = FastText.load(os.path.dirname(
            os.path.abspath(__file__)) + '/fasttext_model/ft_sg.model')
        # self.cbow_model = FastText.load('model/ft_cbow.model')

    def get_similar_words(self, word, sg=1):
        try:
            word_list = self.sg_model.wv.most_similar(positive=[word])
            print(word_list)
            return word_list
        except Exception as e:
            print(e)
            return []
