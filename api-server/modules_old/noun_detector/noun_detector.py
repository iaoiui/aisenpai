import MeCab
import json
import os


class MecabWrapper():
    def __init__(self):
        self.tagger = MeCab.Tagger(
            '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
        self.dic_path = os.path.dirname(
            os.path.abspath(__file__)) + '/data/qiita_tag.json'

    def get_noun(self, sentence, use_dic=False):
        # 名詞抜き出し
        self.tagger.parse('')
        node = self.tagger.parseToNode(sentence)
        queries = []
        while node:
            if node.feature.split(',')[0] == '名詞':
                queries.append(node.feature.split(',')[6].lower())
            node = node.next
        print(queries)

        results = []
        for query in queries:
            if(use_dic):
                # タグ一覧に検索語が含まれるかどうかチェック
                dic = open(self.dic_path)
                tags = json.load(dic)
                for tag in tags:
                    if query == tag['id']:
                        results.append(query)
            else:
                results.append(query)

        return results
