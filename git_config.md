## Global setting for Gitee:

git config --global user.name "bfcatlu"

git config --global user.email "bfcat@qq.com"

git config --global credential.helper store

## Check config list
git config --list

git remote -v

if not remote setting, add below

git remote add origin https://gitee.com/bfcatlu/tsalab.git 

## Pull & Push

git pull origin master  # for the first time

git push origin master  # necessary step For new repository

## Fix long path problem
git config --global core.longpaths true