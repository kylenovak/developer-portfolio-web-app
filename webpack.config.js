const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const LiveReloadPlugin = require('webpack-livereload-plugin');

const config = {
    entry: './kylejnovak/static/src/main.tsx',
    devtool: 'source-map',
    module: {
        loaders: [
            {
                test: /\.tsx?$/,
                loader: 'ts-loader'
            },
            {
                test: /\.scss$/,
                loader: ExtractTextPlugin.extract(
                    'style', 'css!sass'
                )
            }
        ]
    },
    output: {
        path: './kylejnovak/static/dist',
        filename: 'bundle.js'
    },
    plugins: [
        new webpack.optimize.UglifyJsPlugin(),
        new ExtractTextPlugin('bundle.css'),
        new LiveReloadPlugin()
    ],
    resolve: {
        extensions: ['', '.ts', '.tsx', '.js']
    },
    externals: {
        'react': 'React',
        'react-dom': 'ReactDOM'
    },
};

module.exports = config;