from ..models.cache_model import EtcdWrapper
from flask import Blueprint, request, jsonify


app = Blueprint("cache", __name__)


@app.route("/api/v1/dev/etcd")
def etcd_test():
    key = request.args.get("key")
    response = {}
    value = EtcdWrapper().etcd.get(key)
    if EtcdWrapper().cache_exists(key):
        response = {"key": key, "value": value[0].decode()}
    else:
        print("cache doesn't exists")
        # TODO create cache
        # etcd.put(key, synonyms)

    return jsonify(response)
