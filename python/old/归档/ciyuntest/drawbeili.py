import pymysql.cursors
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password='root', db='testbl', charset='utf8', cursorclass = pymysql.cursors.DictCursor)

cursor = conn.cursor()

sql = "select realname from t_s_base_user;"
cursor.execute(sql)

result = cursor.fetchall()

namelist = []
for data in result:
    namelist.append(data['realname'])

print(len(namelist))

# name_text = namelist
name_text = ' '.join(namelist)
print(name_text)

# coloring = np.array(Image.open("zhufu.jpg"))
my_wordcloud = WordCloud(width=1024, height=900,  background_color="white", max_words=2000,
                         mask=None, max_font_size=40, random_state=60, scale=1,
                         font_path="DroidSansFallbackFull.ttf", stopwords=STOPWORDS.add("猴年")).generate(name_text)


plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()