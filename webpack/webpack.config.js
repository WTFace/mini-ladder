const path = require('path');
const JavaScriptObfuscator = require('webpack-obfuscator');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, '../canvas/static/canvas')
  },
  plugins: [
  new JavaScriptObfuscator({
    rotateUnicodeArray: true
  }, [])
  ]
};
