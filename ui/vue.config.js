module.exports = {
  transpileDependencies: ['vuetify'],
  devServer: {
    port: 8080,
    disableHostCheck: true,
    proxy: {
      '/api': {
        target: 'http://server:3000'
      }
    }
  }
}
