#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
import pandas as pd

# 登录微信
# hotReload=True  # 使用这个属性，生成一个静态文件itchat.pkl，用于存储登陆的状态。
itchat.auto_login(hotReload=True, enableCmdQR=2)

# 好友基本信息
friends = itchat.get_friends(update=True)