const express = require('express')
const router = express.Router()
const Logger = require('../common/logger')

router.post('/logger', (req, res, next) => {
  Logger.getLogger().info('start POST /logger')
  try {
    Logger.getLogger().info(req.body)
    res.end()
  } catch (e) {
    Logger.getLogger().error(e)
    res.status(500).end()
  } finally {
    Logger.getLogger().info('end POST /logger')
  }
})

module.exports = router
