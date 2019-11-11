const express = require('express')
const path = require('path')
const cookieParser = require('cookie-parser')
const logger = require('morgan')
const helmet = require('helmet')

const indexRouter = require('./routes/index')

const appLogger = require('./logger')
global.logger = appLogger
appLogger.info('Server Start')

const app = express()

app.use(logger('dev'))
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
app.use(cookieParser())
app.use(express.static(path.join(__dirname, 'public')))
app.use(helmet())

app.use('/api', indexRouter)

module.exports = app
