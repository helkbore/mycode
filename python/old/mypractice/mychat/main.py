import itchat
from common12.func import mkdir

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[0:]
# print(friends)


# 初始化计数器
male = female = other = 0
# for i in friends:
#     print(i)

for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 计算朋友总数
total = len(friends[1:])

# 打印出自己的好友性别比例
print("男性好友: %.2f%%" % (float(male)/total * 100) + "\n" +
      "女性好友: %.2f%%" % (float(female) / total * 100) + "\n" +
      "不明性别好友: %.2f%%" % (float(other) / total * 100) + "\n"
      )

# 定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


#调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var('NickName')
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')



from pandas import DataFrame
data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)


import re
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)


import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

# print(word_space_split)


import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

# coloring = np.array(Image.open("./mychat/wechat.jpg"))#自定义词云的图片
# my_wordcloud = WordCloud(
#                     background_color="white",
#                     max_words=2000,
#                     mask=coloring,
#                     max_font_size=60,
#                     random_state=42,
#                     font_path='C:/windows/fonts/SimHei.ttf',scale=2).generate(word_space_split)
#                     # wget http://labfile.oss.aliyuncs.com/courses/756/DroidSansFallbackFull.ttf中文字符文件

coloring = np.array(Image.open(u"E:\\pythonCode\\pycharm\\test\Me\\mypractice\\mychat\\wechat2.jpg"))
# print(coloring)
my_wordcloud = WordCloud(
                    background_color="white",
                    max_words=2000,
                    mask=coloring,
                    max_font_size=60,
                    random_state=42,
                    scale=2,
                    font_path="E:\\pythonCode\\pycharm\\test\Me\\mypractice\\mychat\\font\\DroidSansFallbackFull.ttf").generate(word_space_split
                )

# image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()

image_colors = ImageColorGenerator(coloring)
mage_colors = ImageColorGenerator(coloring)
plt.figure("wechat_cloud")
plt.imshow(my_wordcloud, cmap=plt.cm.gray, interpolation="bilinear")
plt.imshow(my_wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
plt.close()

#保存图片
path_image = "./image/"
mkdir(path=path_image)
file_name_p =  path_image + 'wechat_cloud.jpg'
my_wordcloud.to_file(file_name_p)