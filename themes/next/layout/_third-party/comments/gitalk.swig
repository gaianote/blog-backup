{% if page.comments && theme.gitalk.enable %}
    <link rel="stylesheet" href="https://unpkg.com/gitalk/dist/gitalk.css">
    <script src="https://unpkg.com/gitalk/dist/gitalk.min.js"></script>
    //这两句是调用作者的css和js文件
    <script src="/js/src/md5.min.js"></script>
    <script type="text/javascript">
        var gitalk = new Gitalk({       //这里面的参数我们会在另一个文件中配置
            clientID:  '{{theme.gitalk.clientID}}',
            clientSecret: '{{theme.gitalk.clientSecret}}',
            repo: '{{theme.gitalk.repo}}',
            owner: '{{theme.gitalk.owner}}',
            admin: '{{theme.gitalk.admin}}',
            id: md5(location.pathname),
            distractionFreeMode: '{{theme.gitalk.distractionFreeMode}}',
          })
          gitalk.render('gitalk-container')
    </script>
{% endif %}