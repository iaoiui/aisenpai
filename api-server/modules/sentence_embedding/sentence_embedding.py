from modules.sentence_embedding.bert_juman import BertWithJumanModel
import json
import numpy as np
import os


class BertWrapper():
    def __init__(self):
        self.model_path = os.path.dirname(
            os.path.abspath(__file__)) + '/Japanese_L-12_H-768_A-12_E-30_BPE'
        self.bert = BertWithJumanModel(self.model_path)
        self.title_data_path = os.path.dirname(
            os.path.abspath(__file__)) + '/data/qiita_20**_title_vec_markdown_no_processing.json'

    def get_similar_sentence(self, question):
        question_vec = np.array(self.bert.get_sentence_embedding(question))
        # 比較
        max = -1
        max_obj = {}
        for i in range(11, 20):
            data = open(self.title_data_path.replace('**', str(i)))
            articles = json.load(data)
            # コサイン類似度の高い記事を返す
            for article in articles:
                try:
                    vec = np.array(article['vec'])
                    cos = np.dot(vec, question_vec) / \
                        np.linalg.norm(vec) / np.linalg.norm(question_vec)
                    if cos > max:
                        max = cos
                        max_obj = article
                except:
                    return {'error': 'error'}
        print(max)
        return max_obj
