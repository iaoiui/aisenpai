"""質問の中からQiitaのタグに含まれる名詞を抜き出し、fastTextで関連語を導出するコントローラ"""
from flask import Blueprint, current_app, request, jsonify
from ..models.related_terms_model import FasttextWrapper
from ..models.noun_detect_model import GinzaWrapper
from ..models.cache_model import EtcdWrapper
import json

app = Blueprint("synonym", __name__)


@app.route("/api/v1/synonym")
def get_synonym():
    """
    質問の中からQiitaのタグに含まれる名詞を抜き出し、fastTextで関連語を導出するコントローラ
    """
    logger = current_app.logger
    response = {"words": []}
    try:
        logger.info("start synonym")
        sentence = request.args.get("sentence")

        # 既にキャッシュに結果が存在すれば使い回して高速化
        etcd = EtcdWrapper()
        if etcd.cache_exists(sentence):
            return jsonify(json.loads(etcd.get_cache(sentence)))
        else:
            # GiNZA（SudachiPy）による名詞抽出
            noun_list = GinzaWrapper().get_noun(sentence)
            # fastTextで意味の近い単語を抽出
            get_synonym_core(noun_list, response)
            logger.info("finish synonym")

            # キャッシュに追加
            etcd.put_cache(sentence, response)

            return jsonify(response)

    except Exception as error:
        logger.error(error)
        logger.info("finish synonym")
        return jsonify({"error": "error"})


# TODO 高速化
def get_synonym_core(noun_list, response):
    """
    fastTextで意味の近い単語を抽出
    """
    ft = FasttextWrapper()
    for noun in noun_list:
        similar_words = ft.get_similar_words(noun.lower())
        record = {"keyword": noun, "similarWords": []}
        for similar_word in similar_words:
            record["similarWords"].append(
                {"word": similar_word[0], "value": similar_word[1]}
            )
        response["words"].append(record)
