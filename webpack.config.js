'use strict';

let path = require('path');

module.exports = {
  mode: 'development',
  entry: './static/vendor/js/script.js',
  output: {
    filename: 'bundle.js',
    path: __dirname + '/static/vendor/js'
  },
  watch: true,

  devtool: "source-map",

  module: {}
};
