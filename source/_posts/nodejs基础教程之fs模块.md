---
title: nodejs基础教程之fs模块
date: 2017-04-26 18:14:25
tags: nodejs
---

fs是filesystem的缩写，该模块提供的文件读写能力,几乎对所有操作提供异步和同步两种操作方式，供开发者选择

```javascript
const fs = require('fs')
const fileName = __dirname + '/test.txt'
```

## 文件读写

**文件读取**

`fs.readFile(file[, options], callback)` 异步读取

```javascript
const fs = require('fs')
fs.readFile(__dirname + '/test.txt', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

```
<Buffer 68 65 6c 6c 6f 20 6e 6f 64 65 6a 73 ef bc 81>
```

`fs.readFileSync(file[, options])` 同步读取

```javascript
let fileName = __dirname + '/test.txt'
let data = fs.readFileSync(fileName, 'utf8');
console.log('readFileSync_str:',data)
```

**文件写入**

writeFile方法用于异步写入文件。

```javascript
fs.writeFile(fileName, 'Hello Node.js', 'utf8',(err) => {
  if (err) throw err;
  console.log('It\'s saved!');
});
```

writeFileSync方法用于同步写入文件。

```javascript
fs.writeFileSync(fileName, str, 'utf8');
```

## 目录操作

### mkdir() & mkdirSync()

```javascript
//mode default value 0o777
fs.mkdir(path[, mode], callback)#

//return undefined
fs.mkdirSync(path[, mode])
```

### readdir() & readdirSync()

```javascript
fs.readdir(path, function(err,files){
  if (err) throw err;
  console.log(files);
})

fs.readdirSync(path)
```

`files`是一个包含了文件或目录名的数组

```
['readdir.js','readFile.js','stat.js','test.txt','writeFile.js' ]
```

## fs.stat

我们可以通过fs.stat用于得到文件信息，判断文件是否存在，以及是文件还是目录

```javascript
fs.stat(fileName,(err,stats)=>{
  console.log(stats)
})
```

如果文件不存在，输出`undefined`，如果文件存在，输出以下信息：

```
{
  dev: 2114,
  ino: 48064969,
  mode: 33188,
  nlink: 1,
  uid: 85,
  gid: 100,
  rdev: 0,
  size: 527,
  blksize: 4096,
  blocks: 8,
  atime: Mon, 10 Oct 2011 23:24:11 GMT,
  mtime: Mon, 10 Oct 2011 23:24:11 GMT,
  ctime: Mon, 10 Oct 2011 23:24:11 GMT,
  birthtime: Mon, 10 Oct 2011 23:24:11 GMT
}
```

stats的方法

```javascript
stats.isFile()
stats.isDirectory()
stats.isBlockDevice()
stats.isCharacterDevice()
stats.isSymbolicLink() (only valid with fs.lstat())
stats.isFIFO()
stats.isSocket()
```

## watchfile() & unwatchfile()

`watchfile`方法监听一个文件，如果该文件发生变化，就会自动触发回调函数。

```javascript
var fs = require('fs');

fs.watchFile('message.text', (curr, prev) => {
  console.log(`the current mtime is: ${curr.mtime}`);
  console.log(`the previous mtime was: ${prev.mtime}`);
});
```

`unwatchfile`方法用于解除对文件的监听。

## createReadStream()

`createReadStream`方法往往用于打开大型的文本文件，创建一个读取操作的数据流。所谓大型文本文件，指的是文本文件的体积很大，读取操作的缓存装不下，只能分成几次发送，每次发送会触发一个`data`事件，发送结束会触发`end`事件。

```javascript
let input = fs.createReadStream(fileName);
input.on('start',() => {console.log('start')})
input.on('data',(data) =>{
  console.log(data)
})
input.on('end', () => {console.log('end')})
```

`createWriteStream`方法创建一个写入数据流对象，该对象的`write`方法用于写入数据，`end`方法用于结束写入操作。

```javascript
var out = fs.createWriteStream(fileName, {
  encoding: 'utf8'
});
out.write(str);
out.end();
```

`createWriteStream`方法和`createReadStream`方法配合，可以实现拷贝大型文件。

```javascript
function fileCopy(filename1, filename2, done) {

  var input = fs.createReadStream(filename1);
  var output = fs.createWriteStream(filename2);

  input.on('data', (d) => { output.write(d); });
  input.on('error', (err) => { throw err; });
  input.on('end', () => {
    output.end();
    if (done) done();
  });
}
```

## pipe()

就像可以把两个水管串成一个更长的水管一样，两个流也可以串起来。一个Readable流和一个Writable流串起来后，所有的数据自动从Readable流进入Writable流，这种操作叫pipe。

在Node.js中，Readable流有一个 `pipe()` 方法，就是用来干这件事的。

让我们用 `pipe()` 把一个文件流和另一个文件流串起来，这样源文件的所有数据就自动写入到目标文件里了，所以，这实际上是一个复制文件的程序：

```javascript
const fs = require('fs');

const rs = fs.createReadStream('sample.txt');
const ws = fs.createWriteStream('copied.txt');

rs.pipe(ws);
```

默认情况下，当Readable流的数据读取完毕，end事件触发后，将自动关闭Writable流。如果我们不希望自动关闭Writable流，需要传入参数：

```javascript
readable.pipe(writable, { end: false });
```

