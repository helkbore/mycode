import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np
import PIL.Image as Image
import random


'''附加文件: '''
stopwords_path = 'stopwords.txt'
text_path = 'chunjie.txt'
img_path = "wechat.jpg"
font_path = 'DroidSansFallbackFull.ttf'


mywordlist = []

f = open(text_path, encoding='utf-8')
text = f.read()


# jieba分词
# seg_list = jieba.cut(text, cut_all=False, HMM=True)
tags = jieba.analyse.extract_tags(text, 2000, withWeight=False)
seg_list = []
for item in tags:
    seg_list.append(item)
    # print(item)
liststr = '/'.join(seg_list)
# exit()

# 停用词文件导入 -- 我又针对导入文本加了一些...
f_stop = open(stopwords_path, encoding='utf-8')
f_stop_text = f_stop.read()
f_stop_seg_list = f_stop_text.split('\n')
# print(f_stop_text)

mywordlist.append("~~~~~2018嘉婧给大家拜年啦~~~~~")


# 过滤掉停用词
for myword in liststr.split('/'):
    if not(myword.strip() in f_stop_seg_list) and len(myword.strip())> 1:
        mywordlist.append(myword)
        # mywordlist.append("嘉婧")



text_result = ' '.join(mywordlist)
# print(len(text_result))
# print(text_result)



# print(text)
# exit()

# for key in jieba.analyse.extract_tags(text, 60, withWeight=False):
#     print(key)
# exit()

# seg_list = jieba.cut_for_search(text, HMM=False)
# print(", ".join(seg_list))



# zhufulist = jieba.cut(text, cut_all=False, HMM= True)
# zhufulist = jieba.cut(text, cut_all=True, HMM= False)
# zhufulist = jieba.cut(text, cut_all=False, HMM= True)
# zhufu = " ".join(zhufulist)
# print(len(zhufu))
# # exit()





coloring = np.array(Image.open("wechat.jpg"))
my_wordcloud = WordCloud(width=1024, height=900, ranks_only=True, background_color="white", max_words=2000,
                         mask=coloring, max_font_size=40, random_state=60, scale=2,
                         font_path="DroidSansFallbackFull.ttf", stopwords=STOPWORDS.add("猴年")).generate(text_result)

image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# # plt.show()
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "rgb(%d, %d, %d)" % (random.randint(250, 255), random.randint(0, 255), random.randint(0, 255))

# grey_color_func()
# exit()

# 直接画, 多彩的
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 根据底图画, 颜色一致
plt.imshow(my_wordcloud.recolor(color_func=grey_color_func, random_state=3))
plt.axis("off")
plt.show()

# 自定义色彩
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.axis("off")
plt.show()
# plt.figure()

# plt.imshow(coloring, cmap=plt.cm.gray)
# plt.axis("off")
# plt.show()