const express = require('express')
const router = express.Router()
const loginController = require('../controllers/login_controller')

router.post('/login', (req, res, next) => loginController.login(req, res, next))

module.exports = router
