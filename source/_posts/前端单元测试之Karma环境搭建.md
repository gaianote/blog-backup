title: 前端单元测试之Karma环境搭建
author: 李云鹏
date: 2018-09-20 02:49:02
tags:
---
## 前言

在前端开发中，测试常常是被忽略的一环。因此最近在研究前端自动化测试框架Karma，把个人的学习过程分享出来，希望对大家有帮助。

## 什么是Karma？

Karma是由Google团队开发的一套前端测试运行框架。它不同于测试框架（例如jasmine，mocha等），运行在这些测试框架之上。主要完成一下工作：

* Karma启动一个web服务器，生成包含js源代码和js测试脚本的页面；

* 运行浏览器加载页面，并显示测试的结果；

* 如果开启检测，则当文件有修改时，执行继续执行以上过程。


## Karma的安装配置

### 初始项目结构


      
```
karma-example
    ├── src
         ├── index.js
    ├── test
    ├── package.json

```

index.js的内容如下


      
```
function isNum(num) {
  if (typeof num === 'number') {
    return true
  } else {
    return false
  }
}
```

### 安装Karma环境

为了方便搭建Karma环境，我们可以全局安装`karma-cli`来帮我们初始化测试环境：


      
```
npm i -g karma-cli

```

然后在项目中安装karma包


      
```
npm i --save-dev karma

```

接下来在工程目录中运行`karma init`来进行测试环境初始化，并按照指示一步步完成。

![img](https://segmentfault.com/img/bVC39F?w=763&amp;h=561)


上图是选项的示例，这里使用jasmine测试框架，PhantomJS作为代码运行的环境（也可以选择其他浏览器作为运行环境，比如Chrome，IE等）。最后在项目中生成karma.conf.js文件。

至此就搭建好了基本的Karma运行环境。

### 运行Karma

在test目录里编写一个简单的测试脚本，我们使用的是jasmine测试框架，具体的api可以参考[jasmine api](http://jasmine.github.io/2.5/introduction.html)，内容如下


      
```
describe('index.js: ', function() {
  it('isNum() should work fine.', function() {
    expect(isNum(1)).toBe(true)
    expect(isNum('1')).toBe(false)
  })
})
```

然后在项目根目录下运行`karma start`命令,我们可以看到运行的结果如下

![img](https://image-static.segmentfault.com/305/967/3059671490-57d6956eef629_articlex)


可以看到，运行的结果显示测试成功。

同时，因为我们之前设置了监控文件的修改，所以当我们修改源文件或者测试脚本的时候，Karma会自动帮我们再次运行，无需我们手动操作。

### Coverage

如何衡量测试脚本的质量呢？其中一个参考指标就是代码覆盖率（coverage）。

什么是代码覆盖率？简而言之就是测试中运行到的代码占所有代码的比率。其中又可以分为行数覆盖率，分支覆盖率等。具体的含义不再细说，有兴趣的可以自行查阅资料。

虽然并不是说代码覆盖率越高，测试的脚本写得越好（可以看看参考文献4），但是代码覆盖率对撰写测试脚本还是有一定的指导意义的。因此接下来我们在Karma环境中添加Coverage。

首先安装好Karma覆盖率工具


      
```
npm i --save-dev karma-coverage

```

然后修改配置文件karma.conf.js，


      
```

module.exports = function(config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine'],
    files: [
      'src/**/*.js',
      'test/**/*.js'
    ],
    exclude: [],

    // modified
    preprocessors: {
        'src/**/*.js': ['coverage']
    },

    //modified
    reporters: ['progress', 'coverage'],

    // add
    coverageReporter: {
      type : 'html',
      dir : 'coverage/'
    },

    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['PhantomJS'],
    singleRun: false,
    concurrency: Infinity
  })
}

```

再运行`karma start`后，会在目录下生成coverage目录，里面有本次测试的覆盖报告。打开后的结果如下

![img](https://image-static.segmentfault.com/329/031/3290314682-57d69de262f9c_articlex)


### 使用Webpack+Babel

在实际项目中，有事会需要用到Webpack和ES6，所以接下来将Webpack和Babel集成进Karma环境中。

安装karma-webpack


      
```
npm i --save-dev karma-webpack

```

安装babel


      
```
npm i --save-dev babel-loader babel-core babel-preset-es2015

```

然后文件进行改造，`src/index.js`文件修改为


      
```
function isNum(num) {
  if (typeof num === 'number') {
    return true
  } else {
    return false
  }
}

exports.isNum = isNum

```

`text/index.js`文件修改为


       {  it('isNum() should work fine.', () => {    expect(Util.isNum(1)).toBe(true)    expect(Util.isNum('1')).toBe(false)  })})" title="" data-original-title="复制">
```
const Util = require('../src/index')

describe('index.js: ', () => {
  it('isNum() should work fine.', () => {
    expect(Util.isNum(1)).toBe(true)
    expect(Util.isNum('1')).toBe(false)
  })
})

```

接下来修改配置文件karma.conf.js


      
```
module.exports = function(config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine'],
    files: [
      'test/**/*.js'
    ],
    exclude: [],
    preprocessors: {
      'test/**/*.js': ['webpack', 'coverage']
    },
    reporters: ['progress', 'coverage'],
    coverageReporter: {
      type: 'html',
      dir: 'coverage/'
    },
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    browsers: ['PhantomJS'],
    singleRun: false,
    concurrency: Infinity,
    webpack: {
      module: {
        loaders: [{
          test: /\.js$/,
          loader: 'babel',
          exclude: /node_modules/,
          query: {
            presets: ['es2015']
          }
        }]
      }
    }
  })
}

```

注意这里的修改：

* files只留下test文件。因为webpack会自动把需要的其它文件都打包进来，所以只需要留下入口文件。

* preprocessors也修改为test文件，并加入webpack域处理器

* 加入webpack配置选项。可以自己定制配置项，但是不需要entry和output。这里加上babel-loader来编译ES6代码


运行`karma start`，成功了~

再看看Coverage，卧槽。。居然不是百分之百了。。。

原因很简单，webpack会加入一些代码，影响了代码的Coverage。如果我们引入了一些其它的库，比如jquery之类的，将源代码和库代码打包在一起后，覆盖率会更难看。。这样的Coverage就没有了参考的价值。

还好有大神给我们提供了解决方案，需要安装插件


      
```
npm i --save-dev babel-plugin-istanbul

```

修改webpack中babel-loader的配置


      
```
{
  test: /\.js$/,
  loader: 'babel',
  exclude: /node_modules/,
  query: {
    presets: ['es2015'],
    plugins: ['istanbul']
  }
}

```

因为这里引入了istanbul插件来检测Coverage，所以要把preprocessors里的`coverage`去掉。

搞定以后，运行`karma start`。当当当当~一切OK啦，尽情编写测试脚本把~

最后附上示例项目地址:[karma-example](https://github.com/xiaojimao18/karma-example)

## 参考文档

[前端单元测试之Karma环境搭建](https://segmentfault.com/a/1190000006895064)
