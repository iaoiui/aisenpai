const log4js = require('log4js')
log4js.configure(process.env.LOG4J_CONFIG_FILE)
const logger = log4js.getLogger('app')

module.exports = logger
