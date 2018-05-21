import itchat

itchat.auto_login(hotReload=True)
mps = itchat.get_mps()
for i in mps:
    nickname = i["NickName"] # 公众号名称
    imgurl = i["HeadImgUrl"] # 头像url

