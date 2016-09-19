const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const config = {
    entry: './src/index.tsx',
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
                    'style', // the backup style loader
                    'css?sourceMap!sass?sourceMap'
                )
            }
        ]
    },
    output: {
        path: './static',
        filename: '/bundle.js',
    },
    plugins: [
        new webpack.optimize.UglifyJsPlugin(),
        new ExtractTextPlugin('./bundle.css')
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