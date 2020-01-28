module.exports = {
  transpileDependencies: ['vuetify'],
  devServer: {
    port: 8080,
    disableHostCheck: true,
    proxy: {
      '/api': {
        target: 'http://scenario-server:3000'
      },
      '/socket.io': {
        target: 'ws://scenario-server:3000',
        ws: true
      }
    }
  }
}
