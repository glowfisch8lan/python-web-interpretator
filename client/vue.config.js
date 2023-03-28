const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: '/python-web/',
  pluginOptions: {
    quasar: {
      importStrategy: 'kebab',
      rtlSupport: false
    }
  },
  devServer: {
    proxy: {
      '^/api': {
        target: "http://127.0.0.1:5040/",
        changeOrigin: true,
      },
    }
  },
  transpileDependencies: [
    'quasar'
  ]
})
