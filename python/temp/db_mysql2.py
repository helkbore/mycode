import SQLManager
import myfunc

DB_CONFIG = {
    "host"     : 'localhost',
    "port"     : 3306,
    "user" :'root',
    "password" : "root",
    "db"  : 'favorites',
    "charset"  : "utf8"

}




def save_item(d):
    # 查询是否已存在
    item = getItemByName(d['name'])

    if len(item) == 0:
        # add item
        itemId = addItemByDict(d)
    else:
        itemId = item[0][0]

    if 'tag' in d.keys():
        tag = getTagByName(d['tag'])

        if len(tag) == 0:
            tagId = addTagByDict(d)
        else:
            tagId = tag[0][0]


        itemTag = getItemTag(itemId, tagId)

        if len(itemTag) == 0:
            addItemTag(itemId, tagId)

def save_item2(dList):
    # 查询是否已存在
    # item = getItemByName(d['name'])

    itemInsert = []
    itemTagInsert = []

    itemInsertSql = "insert into item (id, name, root, link) values ( %s, %s, %s, %s )"
    ttSql = "insert into item_tag (itemid, tagid) values (%s, %s)"

    db = SQLManager.SQLManager()

    itemSumA = 0 # 表中已存在的
    itemSumB = 0 # 新插入的
    for d in dList:
        # print("d")
        # print(d)
        sql = "select * from item where name= %s "
        args = (d['name'])

        result = db.get_one(sql, args)

        # print(result)
        if result:
            itemSumA = itemSumA + 1
            itemId = d['id'] = result['id']
            # print(itemId)
            # print('***')
            # print(d['name'])
        else:
            itemSumB = itemSumB + 1
            itemId = d['id'] = myfunc.genid()
            # print(itemId)
            itemInsert.append((d['id'], d['name'], d['root'], d['link']))
            # print('&&&')
            # print(d['name'])
        # print()
        # print(d['name'])
        if 'tag' in d.keys():
            sql = "select * from tag where name= %s"
            args = (d['tag'])

            tag = db.get_one(sql, args)
            if tag:
                tagId = d['tagid'] = tag['id']
            else:
                sql = "insert into tag (name) values ( %s)"
                args = (d['tag'])
                tagId = d['tagid'] = db.create(sql, args)

            sql = "select * from item_tag where itemid=%s and tagid=%s"
            args = (d['id'], d['tagid'])
            # print(args)

            itemTag = db.get_one(sql, args)

            if not itemTag:
                itemTagInsert.append(args)



    # for ii in itemInsert:
    #     print(ii)
    #
    # for mm in itemTagInsert:
    #     print(mm)



    # print(itemInsert)
    if itemInsert:
        db.multi_modify(itemInsertSql, itemInsert)

    if itemTagInsert:
        db.multi_modify(ttSql, itemTagInsert)

    # print("-----------存入数据库")
    # for itemfor in itemInsert:
    #     print(itemfor['name'])

    print()
    print("----------------------------")
    print("处理了" + str(len(dList)) + "项")
    print("已存在条目为: " + str(itemSumA))
    print("新插入条目为: " + str(itemSumB))

    db.close()

    # if len(item) == 0:
    #     # add item
    #     itemId = addItemByDict(d)
    # else:
    #     itemId = item[0][0]
    #
    # if 'tag' in d.keys():
    #     tag = getTagByName(d['tag'])
    #
    #     if len(tag) == 0:
    #         tagId = addTagByDict(d)
    #     else:
    #         tagId = tag[0][0]
    #
    #
    #     itemTag = getItemTag(itemId, tagId)
    #
    #     if len(itemTag) == 0:
    #         addItemTag(itemId, tagId)




# 测试
d1 = {
    "name" : "站长工具",
    "link" : "http://tool.chinaz.com",
    "root" : "http://tool.chinaz.com",
    "tag"  : "实用工具"
}

d2 = {
    "name" : "网站备案",
    "link" : "http://www.miitbeian.gov.cn/publish/query/indexFirst.action/",
    "root" : "http://www.miitbeian.gov.cn",
    "tag"  : "实用工具"
}

d3 = {
    "name" : "域名注册",
    "link" : "https://wanwang.aliyun.com/domain/",
    "root" : "https://wanwang.aliyun.com",
    "tag"  : "实用工具"
}

d4 = {
    "name" : "在线杀毒",
    "link" : "http://webscan.360.cn/",
    "root" : "http://webscan.360.cn",
    "tag"  : "实用工具"
}

d5 = {
    "name" : "二维码",
    "link" : "https://cli.im/",
    "root" : "https://cli.im",
    "tag"  : "实用工具"
}

d6 = {
    "name" : "虚拟主机",
    "link" : "https://www.cndns.com/",
    "root" : "https://www.cndns.com",
    "tag"  : "实用工具"
}

dList = [d1, d2, d3, d4, d5, d6]


# db = SQLManager.SQLManager()
# result = db.get_one("select * from item_tag where tagid = 22")
# print(result)
# db.close()