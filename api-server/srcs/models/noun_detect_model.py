"""テキストの中からQiitaのタグに含まれる名詞を抜き出すモデル"""
import json
from pathlib import Path
from flask import current_app
import spacy


class GinzaWrapper:
    """
    テキストの中からQiitaのタグに含まれる名詞を抜き出すモデルクラス
    """

    def __init__(self):
        self.nlp = spacy.load("ja_ginza")
        self.dic_path = (
            Path(str(current_app.root_path)) / "resources/tags/qiita_tag.json"
        )
        # タグ読み込み
        self.tags = json.load(open(self.dic_path))
        self.logger = current_app.logger

    def get_noun(self, sentence):
        """
        テキストの中からQiitaのタグに含まれる名詞を抜き出すモデルクラス
        """
        try:
            doc = self.nlp(sentence)
            # 名詞抜き出し
            nouns = []
            for sent in doc.sents:
                nouns += filter(lambda e: e.pos_ == "NOUN", sent)
            nouns = list(map(lambda e: e.orth_, nouns))
            # タグに含まれる名詞のみ返却
            results = []
            for noun in nouns:
                for tag in self.tags:
                    if noun == tag["id"]:
                        results.append(noun)

            return results
        except Exception as error:
            self.logger.error(error)
            return []
