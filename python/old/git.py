#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'git使用 2017年11月7日'

'''
1. 安装git
2. 创建版本库
    git init
3. 添加文件到版本库
    git add readme.txt
    git commit -m '备注改动'    
    
'''

'''
git add                     删除,/添加 到暂存区
git rm
git status                  当前状态
git log                     历史版本
git log --pretty=oneline    精简版查看
git diff 文件名              查看做了哪些修改
git reset                   退回到上一个版本
git reflog                  历史记录, 操作记录
git checkout --  文件名      退回最近一次git commit或 git add
git reset HEAD 文件名        撤销暂存区(add)
'''

'''
在Git中，用HEAD表示当前版本，也就是最新的提交
上一个版本就是HEAD^，上上一个版本就是HEAD^^
上100个版本 HEAD~100
'''

'''
命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：

一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次git commit或git add时的状态。
'''

# 远程仓库
'''
1. 创建ssh key
$ ssh-keygen -t rsa -C "helkbore@163.com"
2. 在本地找到id_rsa.pub文件 录入到github中
3. 在github上建版本库
4. 连接远程
$ git remote add origin git@github.com:michaelliao/learngit.git
5. 把本地库的所有内容推送到远程库上
$ git push -u origin master
6. 本地提交到远程
$ git push origin master
'''

# 远程库克隆到本地
'''
$ git clone git@github.com:helkbore/gitskills.git
'''

# 分支相关
'''
查看分支：git branch

创建分支：git branch <name>

切换分支：git checkout <name>

创建+切换分支：git checkout -b <name>

合并某分支到当前分支：git merge <name>

删除分支：git branch -d <name>

查看分支合并情况
$ git log --graph --pretty=oneline --abbrev-commit

--no-ff 合并 
$ git merge --no-ff -m "merge with no-ff" dev
'''

# 工作场景储存
'''
分支1
$ git stash
$ git checkout 分支2
修改编辑, add, commit之后删除分支2 回到分支1

$ git stash list
$ git stash pop
'''

# 多人协作
'''
查看远程库信息，使用git remote -v；

本地新建的分支如果不推送到远程，对其他人就是不可见的；

从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；

在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；

建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；

从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
'''

# 标签
'''
命令git tag <name>用于新建一个标签，默认为HEAD，也可以指定一个commit id；

git tag -a <tagname> -m "blablabla..."可以指定标签信息；

git tag -s <tagname> -m "blablabla..."可以用PGP签名标签；

命令git tag可以查看所有标签。



远程标签
命令git push origin <tagname>可以推送一个本地标签；

命令git push origin --tags可以推送全部未推送过的本地标签；

命令git tag -d <tagname>可以删除一个本地标签；

命令git push origin :refs/tags/<tagname>可以删除一个远程标签。
'''
