const loginModel = require('../models/login_model')
const loginController = {}

loginController.login = (req, res, next) => {
  loginModel.login()
}

module.exports = loginController
