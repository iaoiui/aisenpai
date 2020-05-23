const messageModel = require('../models/message_model')
const messageController = {}

messageController.login = (req, res, next) => {
  messageModel.createMessage()
}

module.exports = messageController
