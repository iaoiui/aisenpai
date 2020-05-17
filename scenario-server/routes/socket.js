const axios = require('axios')
const Logger = require('../common/logger')

const callbackSocketIO = socket => {
  Logger.getLogger().info('connected')

  // 新規接続時にウェルカムメッセージを送信
  socket.on('welcome', msg => {
    socket.emit('message', global.WELCOME_MESSAGE)
    console.log(msg)
  })

  // メッセージ受信
  socket.on('message', async msg => {
    try {
      // 時間がかかった時用のクッションメッセージ
      socket.emit('message', global.WAIT_MESSAGE)

      // 検索クエリを投げかけて関連記事を得る
      const title = await axios.get('http://api-server:5000/sentence', { params: { sentence: msg } })
      console.log(title.data.title)

      // 記事本文を得る
      const body = await axios.get('http://api-server:5000/qiita', { params: { sentence: title.data.title } })
      console.log(body.data.body)

      // 記事要約
      const summary = axios.get('http://api-server:5000/summary', { params: { sentence: body.data.body } })
      console.log(summary)

      // 関連単語取得
      const words = axios.get('http://api-server:5000/word', { params: { sentence: msg, useDictionary: true } })
      console.log(words)

      const p = await Promise.all([summary, words])

      const result = {
        summary: p[0].data.body,
        words: p[1].data.words,
        title: title.data.title,
        url: ''
      }

      socket.emit('message', result)
    } catch (error) {
      Logger.getLogger().error(JSON.stringify(error, null, 2))
      // エラー時のメッセージ
      socket.emit('message', global.FAIL_MESSAGE)
    }

    console.log(msg)
  })
}

module.exports = callbackSocketIO
