import itchat

# 登录
# itchat.auto_login()
itchat.auto_login(hotReload=True)

# 给文件传输助手发一条信息
itchat.send("Hello, filehelper", toUserName='filehelper')

# 回复发给自己的文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text + "本人正在测试微信接口自动回复功能~"

# itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]
print(friends[0]['NickName'])
itchat.run()
