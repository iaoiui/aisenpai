"""質問の中からQiitaのタグに含まれる名詞を抜き出し、fastTextで関連語を導出するコントローラ"""
from flask import Blueprint, current_app, request, jsonify
from ..models.related_terms_model import FasttextWrapper
from ..models.noun_detect_model import GinzaWrapper
import etcd3
import json

app = Blueprint("synonym", __name__)

# etcd 初期化
etcd = etcd3.client(host="etcd", port=2379)


@app.route("/api/v1/dev/etcd")
def etcd_test():
    key = request.args.get("key")
    response = {}
    value = etcd.get(key)
    if cache_exists(key) is True:
        response = {"key": key, "value": value[0].decode()}
    else:
        print("cache doesn't exists")
        # TODO create cache
        # etcd.put(key, synonyms)

    return jsonify(response)


def get_cache(key):
    value = etcd.get(key)
    return value[0].decode()


def put_cache(key, value):
    jsonstring = json.dumps(value, ensure_ascii=False)
    etcd.put(key, jsonstring)


def cache_exists(key):
    value = etcd.get(key)
    if value[0] is None:
        # cache doesn't exist
        return False
    else:
        return True


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
        if cache_exists(sentence) is True:
            return jsonify(json.loads(get_cache(sentence)))
        else:
            # GiNZA（SudachiPy）による名詞抽出
            noun_list = GinzaWrapper().get_noun(sentence)
            get_synonym_core(noun_list, response)
            logger.info("finish synonym")

            # キャッシュに追加
            put_cache(sentence, response)

            return jsonify(response)

    except Exception as error:
        logger.error(error)
        logger.info("finish synonym")
        return jsonify({"error": "error"})


# TODO 高速化
def get_synonym_core(noun_list, response):
    ft = FasttextWrapper()
    for noun in noun_list:
        similar_words = ft.get_similar_words(noun.lower())
        record = {"keyword": noun, "similarWords": []}
        for similar_word in similar_words:
            record["similarWords"].append(
                {"word": similar_word[0], "value": similar_word[1]}
            )
        response["words"].append(record)
