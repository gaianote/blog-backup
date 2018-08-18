# gaianote.github.io

## 快速开始

1. 安装最新版本的 node.js ，注意安装时必须勾选 `add to path`
2. 运行`npm install hexo-cli -g` 安装命令行工具
3. 运行`git clone git@github.com:gaianote/gaianote.github.io.git`，将source分支clone到本地
4. cd到项目根目录，运行 `npm install` 安装相关依赖
5. `hexo server` 启动服务器，可以在本地浏览blog

## 云端推送

当我们需要更新blog时，运行以下命令即可完成推送本地blog到github中

```bash
$ hexo generate
$ hexo deploy
```

通过以上命令，系统会自动执行以下操作：

1. 生成html静态文件
2. 将生成的静态文件发布到master分支上(无需使用git切换到master分支)
3. 将blog源文件分支提交到source分支上(shelljs实现)

## 注意事项

本博客程序中的package依赖固定的版本号，当你直接更新某个主题或者依赖包时，可能会导致运行故障。因此，在博客展示正常的情况下，不建议对版本进行更新。