const express = require('express')
const router = express.Router()
const uuidv4 = require('uuid/v4')

router.get('/test', (req, res, next) => {
  const uuid = uuidv4()
  global.logger.info(`${uuid} start GET /test`)
  try {
    res.send(uuid)
  } catch (e) {
    global.logger.error(`${uuid} error`)
    const errObj = {
      code: 'E000001',
      msg: e,
      id: uuid
    }
    global.logger.error(`${uuid} ${errObj.code}`)
    global.logger.error(`${uuid} ${errObj.msg}`)
    global.logger.error(`${uuid} ${errObj.id}`)
    res.status(500).send(errObj)
  } finally {
    global.logger.info(`${uuid} end GET /test`)
  }
})

module.exports = router
