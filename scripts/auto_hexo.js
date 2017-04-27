/**
 * hexo 自动脚本备份
 * 当在bash输入 $ hexo g 时，自动执行 hexo d ; git add . ;git commit -m "update" ; git push
 */

require('shelljs/global');

var path = require('path');

try {

  hexo.on('generateAfter', function() {

    run();

  });

} catch (e) {

  console.log("产生了一个错误<(￣3￣)> !，错误详情为：" + e.toString());

}

function run() {

  if (!which('git')) {
    echo('Sorry, this script requires git');
    exit(1);
  } else {
    echo("======================Auto Backup Begin===========================");

    cd(process.cwd());

    if (exec('hexo d').code !== 0) {
      echo('Error: hexo generate failed');
      exit(1);
    }

    if (exec('git add --all').code !== 0) {
      echo('Error: Git add failed');
      exit(1);

    }
    if (exec('git commit -m "update"').code !== 0) {
      echo('Error: Git commit failed');
      exit(1);

    }
    if (exec('git push origin source').code !== 0) {
      echo('Error: Git push failed');
      exit(1);

    }
    echo("==================Auto Backup Complete============================")
  }
}

/* 新建文章自动打开编辑器 */
try {
  hexo.on('new', function(data) {//当deploy完成后执行备份
    exec(data.path)
  });
} catch (e) {
  console.log("产生了一个错误<(￣3￣)> !，错误详情为：" + e.toString());
}

