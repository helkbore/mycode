import SQLManager
import myfunc
import time

def saveResult(dList):
    itemList = []
    tagList = []
    itemTagList = []

    # 处理原始dList参数
    for d in dList:
        item = {}
        item['id'] = ""
        item['name'] = d['name']
        item['link'] = myfunc.ifNullValue(d['link'])
        item['root'] = myfunc.get_root(item['link'])
        item['updatetime'] = time.time()
        item['fromurl'] = d['fromurl']

        itemList.append(item)

        tag = d['tag']

        tIndex = []

        # print(tag)
        if tag:
            tempTag = {}
            if type(tag) == str:
                if tag not in tagList:
                    tempTag['id'] = ""
                    tempTag['name'] = tag
                    tagList.append(tempTag)
                tIndex.append(tagList.index(tempTag))

            if type(tag) == list:
                for t in tag:
                    if t not in tagList:
                        tempTag['id'] = ""
                        tempTag['name'] = t
                        tagList.tempTag(tempTag)
                    tIndex.append(tagList.index(t))

        itemTag = {**item, **{'index': tIndex}}
        itemTagList.append(itemTag)

    db = SQLManager.SQLManager()
    # 获取 itemId
    for i in itemList:
        sql = "select id from item where name = %s"
        args = i['name']
        result = db.get_one(sql, args)

        if result:
            itemList[itemList.index(i)]['id'] = result['id']
        else:
            itemList[itemList.index(i)]['id'] = myfunc.genid()
        # print(itemList)

    # 获取tagId

    for i in range(len(tagList)):
        sql = "select id from tag where name= %s"
        args = tagList[i]['name']
        result = db.get_one(sql, args)

        if result:
            tagList[i]['id'] = result['id']
        else:
            tagList[i]['id'] = myfunc.genid()


    # 获取itemTagId

    for i in range(len(itemTagList)):
        sql = "select id from item_tag where itemid = %s and tagid = %s"
        for m in itemTagList[i]['index']:
            args = (itemList[i]['id'], tagList[m])
            result = db.get_one(sql, args)

            if result:
                itemTagList[i]['id'] = result['id']
            else:
                itemTagList[i]['id'] = myfunc.genid()


    sql = "replace into item (id, name, link, root, updatetime, fromurl) values()"
    for i in itemList:
        print(i)

    pass