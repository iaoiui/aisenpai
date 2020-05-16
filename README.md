# AI SENPAI
An Interactive System for Educating Newbie Powered by AI: AI SENPAI.  
AIを搭載した新人教育対話システム。

## 開発

1. VSCodeで開く。
1. 新しいウィンドウでRemote-Containers: Open Folder in Container...で`ui`を選択
1. 新しいウィンドウでRemote-Containers: Open Folder in Container...で`scenario-server`を選択
1. 新しいウィンドウでRemote-Containers: Open Folder in Container...で`api-server`を選択
1. `ui`コンテナと`scenario-server`コンテナそれぞれで`npm i`
1. `api-server`コンテナで`pip install -r requirements.txt`
1. `ui`コンテナの中で`vue ui -H 0.0.0.0`  
Vue CLI UIが`localhost:12222`で参照可能
1. UIを操作してdevサーバを起動  
    1. インポート
    1. このフォルダをインポートする
    1. タスク
    1. serve
    1. パラメータ
    1. ホストの指定→0.0.0.0
    1. 保存
    1. タスクの実行  
フロントエンドのVueのdevサーバが`https://localhost:13333`で参照可能
1. `scenario-server`コンテナの中で`node bin/www`  
1. `api-server`コンテナの中で`python app.py`  

バックエンドのExpressサーバは`localhost:14444`で参照可能
テキスト分析のFlaskサーバは`localhost:15555`で参照可能


