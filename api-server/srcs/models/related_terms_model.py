"""関連語を導出するモデル"""
from pathlib import Path
from gensim.models.fasttext import FastText
from flask import current_app


class FasttextWrapper:
    """
    関連語を導出するモデルクラス
    """

    def __init__(self):
        self.model_path = str(
            Path(str(current_app.root_path)) / "resources/fasttext_model/ft_sg.model"
        )
        self.sg_model = FastText.load(self.model_path)
        self.logger = current_app.logger

    def get_similar_words(self, word):
        """
        関連語を導出するモデルクラス
        """
        try:
            word_list = self.sg_model.wv.most_similar(positive=[word])
            return word_list
        except Exception as error:
            self.logger.error(error)
            return []
