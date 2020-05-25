'''テキストの中からQiitaのタグに含まれる名詞を抜き出すモデル'''
import json
import os
import spacy


class GinzaWrapper():
    '''
    テキストの中からQiitaのタグに含まれる名詞を抜き出すモデルクラス
    '''

    def __init__(self):
        self.nlp = spacy.load('ja_ginza')
        self.dic_path = '../../resources/tags/qiita_tag.json'

    def get_noun(self, sentence):
        '''
        テキストの中からQiitaのタグに含まれる名詞を抜き出すモデルクラス
        '''
        doc = self.nlp(sentence)
        # 名詞抜き出し
        nouns = filter(lambda e: e.pos == 'NOUN', doc)
        # タグ読み込み
        tags = json.load(open(self.dic_path))
        # タグに含まれる名詞のみ返却
        results = []
        for noun in nouns:
            for tag in tags:
                if noun == tag['id']:
                    results.append(noun)

        return results
