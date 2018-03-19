### 319git ubantu

```python
安装一个ubantu系统，又详细的看了下git
在新的ubantu系统上装了个git 基础的linux命令都不太会用了，比如vim的基本命令和查看id_rsa.pub 的密钥，用cat 就好，不需要用vim ，黏贴过去也是格式错误！！

git config --global user.lyasme
git config --global user.email 1250823345@qq.com
cd Desktop/
git clone git@github.com:lyasme/shengxian.git

git push //从远程到本地
git push origin master //从本地到远程

本地操作：mkdir test  cd test
git init //本地创建本地仓库

本地分三个部分：工作区，仓库区，暂存区，其中暂存，仓库区是版本库的部分
git add hello.txt  //加到暂存区
git commit -m '备注信息' //加到仓库区
git push origin master //传送到远程服务器。
git log //查看上传日志
git log --pretty=oneline //简版显示
git reflog //历史命令
git status //查看状态
git rm 文件名 //删除文件
git commit -m '备注信息' //
git pull //把远端代码传到本地

git reset HEAD^版本号 //从仓库区到暂存区
git checkout hello.txt //从暂存区回退到工作区



 








```

