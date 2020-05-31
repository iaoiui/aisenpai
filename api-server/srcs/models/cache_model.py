"""キャッシュサーバであるEtcdを操作するモデル"""
import json
import etcd3


class EtcdWrapper:
    """
    キャッシュサーバであるEtcdを操作するモデルクラス
    """

    def __init__(self):
        # etcd 初期化
        self.etcd = etcd3.client(host="etcd", port=2379)

    def get_cache(self, key):
        value = self.etcd.get(key)
        return value[0].decode()

    def put_cache(self, key, value):
        jsonstring = json.dumps(value, ensure_ascii=False)
        self.etcd.put(key, jsonstring)

    def cache_exists(self, key):
        value = self.etcd.get(key)
        if value[0] is None:
            # cache doesn't exist
            return False
        else:
            return True
