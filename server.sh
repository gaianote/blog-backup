# docker run -it -p 4000:4000 -v C:\Users\gaian\OneDrive\blog:/blog hexo

rm -rf /root/gaianote.github.io/source/*
cp -r /blog/* /root/gaianote.github.io/source
sed -i "s/\[.*\].*\/images\//\[img]\(\/images\//g" `grep "\!\[.*\].*/images/" -rl /root/gaianote.github.io/source/_posts/`
sed -i 's/\[.*\].*\\images\\/\[img]\(\/images\//g' `grep '\!\[.*\].*\\\\images\\\\' -rl /root/gaianote.github.io/source/_posts/`
for image in `find /root/gaianote.github.io/source/_posts -regex '.*.png\|.*.jpg\|.*.gif'`
do
	cp $image source/images/
done
git config --global user.email "gaianote311@gmail.com"
git config --global user.name "gaianote"
hexo g
hexo d
hexo s