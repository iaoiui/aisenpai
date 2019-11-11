# Toys wAR

## 開発

1. VSCodeで開く。
1. 新しいウィンドウでRemote-Containers: Open Folder in Container...で`ui`を選択
1. 新しいウィンドウでRemote-Containers: Open Folder in Container...で`server`を選択
1. `ui`コンテナと`server`コンテナそれぞれで`npm i`
1. `ui`コンテナの中で`vue ui --host 0.0.0.0`  
Vue CLI UIが`localhost:2222`で参照可能
1. UIを操作してdevサーバを起動  
    1. インポート
    1. このフォルダをインポートする
    1. タスク
    1. serve
    1. パラメータ
    1. ホストの指定→0.0.0.0
    1. HTTPSを使用する→チェック
    1. 保存
    1. タスクの実行  
フロントエンドのVueのdevサーバが`https://localhost:3333`で参照可能

バックエンドのExpressサーバは`localhost:4444`で参照可能（あまり意識することはない）


## 本番
1. UIを操作してdevサーバを起動  
    1. インポート
    1. このフォルダをインポートする
    1. タスク
    1. build
    1. タスクの実行  
    `dist`にビルド結果が配置される。
```
./startup.sh
```

`Volume`にログや結果が蓄積される。ようにしたい。
