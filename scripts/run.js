require('shelljs/global');
var path = require('path');
try {
  hexo.on('deployAfter', function() {//当deploy完成后执行备份
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