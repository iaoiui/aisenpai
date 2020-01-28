const log4js = require('log4js')

class Logger {
  constructor () {
    log4js.configure(process.env.LOG4J_CONFIG_FILE)
    this.logger = log4js.getLogger('app')
  }

  getLogger () {
    return this.logger
  }
}

module.exports = new Logger()
