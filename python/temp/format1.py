import re

source_path = u"1.txt"

f = open(source_path, encoding="utf-8")
text = f.read()

# print(text)


# 去除多余换行
text = re.sub(r'\n\n', '', text)
text = re.sub(r'\n\s\(', ' (', text)
print(text)

# p = re.compile(r'\d{1,2}\)[\s\S]*\)')
# print(p.findall(text))

list_link = []
p1 = re.compile(r'\(\s+\S+\s+\)')
list_link  = p1.findall(text)

# print(len(list_link))
# index = 0
# for i in list_link:
#     print(index)
#     index = index + 1
#     print(i)
#     # print(i)
#


p2 = re.compile(r'\d{1,2}\)'+ r'.*?' +r'\(')
t2 = p2.findall(text)

# print(len(t2))
# index = 0
# for i in t2:
#     print(index)
#     index = index + 1
#     print(i)
#     # exit()
# # print(list_link)
# exit()

title = []
for t in t2:
    t = re.sub(r'\d{1,2}\)', "", t)
    t = re.sub(r'\(', "", t)
    title.append(t.strip())
# print(title)

result = []
for i in range(len(title)):
    item = {}

    item['title'] = title[i]
    item['link'] = list_link[i]

    result.append(item)


index = 0
for i in result:
    print(index)
    index = index + 1
    print(i)
    print()
# print(list_link[0])
# print(result)