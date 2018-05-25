import SQLManager
import myfunc
import datetime
import operator

def saveResult(dList):

    itemList = []
    itemDict = []

    tagDict = []
    tagList = []
    itemTagList = []

    repeatItem = 0
    repeatTag = 0
    repeatItemTag = 0

    resultItem = []
    resultTag = []
    resultItemTag = []

    resultItem2 = []
    resultTag2 = []
    resultItemTag2 = []

    find_error = {}
    find_error['item'] = {}
    find_error['item']['name'] = "颜色转换"
    find_error['tag'] = {}
    find_error['tag']['name'] = "Android"

    # 整理item
    for d in dList:
        d['link'] = myfunc.ifNullValue(d['link'])
        d['root'] = myfunc.get_root(d['link'])
        d['updatetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if d['name'].lower() not in itemDict:
            itemDict.append(d['name'].lower())
            itemList.append(d)
        else:
            itemList[itemDict.index(d['name'].lower())]['tag'] = list(set(itemList[itemDict.index(d['name'].lower())]['tag'] + d['tag']))

    db = SQLManager.SQLManager()
    for i in itemList:
        sql = "select id from item where name = %s"
        args = i['name']
        result = db.get_one(sql, args)

        itemDictIndex = itemDict.index(i['name'].lower())

        itemList[itemDictIndex]['itemid'] = "未添加"
        if result:
            repeatItem = repeatItem + 1
            itemList[itemDictIndex]['itemid'] = result['id']
        else:
            itemList[itemDictIndex]['itemid'] = myfunc.genid()


        # 整理tag
        for m in i['tag']:
            tempTag = {}
            tempTag['name'] = m
            tempTag['id'] = ""
            tempTag['fromurl'] = i['fromurl']
            if m.lower() not in tagDict:
                tagDict.append(m.lower())
                tagList.append(tempTag)


        # tag 数据库去重
        for i in range(len(tagList)):
            sql = "select id from tag where name= %s"
            args = tagList[i]['name']
            result = db.get_one(sql, args)

            if result:
                repeatTag = repeatTag + 1
                tagList[i]['id'] = result['id']
            else:
                tagList[i]['id'] = myfunc.genid()
                tagList[i]['id'] = myfunc.genid()


    # 整理item_tag
    for i in itemList:
        for m in i['tag']:
            tempItemTag = {}
            tempItemTag['itemid'] = i['itemid']
            tempItemTag['tagid'] = tagList[tagDict.index(m.lower())]['id']

            # item_tag 数据库去重
            sql = "select id from item_tag where itemid = %s and tagid = %s"
            args = (tempItemTag['itemid'], tempItemTag['tagid'])
            result = db.get_one(sql, args)

            if result:
                repeatItemTag = repeatItemTag + 1
                tempItemTag['id'] = result['id']
            else:
                tempItemTag['id'] = myfunc.genid()
            itemTagList.append(tempItemTag)

    # 构造存入item表数据
    print("---开始存入item表")
    print("共: " + str(len(itemList)) + "条")
    print("重复数据 " + str(repeatItem) + "条")
    tempIndex = 0
    sql = "replace into item (id, `name`, link, root, updatetime) values(%s, %s, %s, %s, %s)"
    sql2 = "update item set `index` = %s where id = %s"
    for i in itemList:
        i['index'] = tempIndex
        tempList = (i['itemid'], i['name'], i['link'], i['root'], i['updatetime'])
        resultItem2.append((i['index'], i['itemid']))

        resultItem.append(tempList)
        tempIndex = tempIndex + 1



    db.multi_modify(sql, resultItem)
    db.multi_modify(sql2, resultItem2)

    # 构造存入tag表数据
    print("---开始存入tag表")
    print("共: " + str(len(tagList)) + "条")
    print("重复数据 " + str(repeatTag) + "条")
    tempIndex = 0
    sql = "replace into tag (fromurl, id, `name`) values (%s, %s, %s)"
    sql2 = "update tag set `index` = %s where id = %s"
    for i in tagList:
        i['index'] = tempIndex

        tempList = (i['fromurl'], i['id'], i['name'])
        resultTag.append(tempList)
        resultTag2.append((i['index'], i['id']))
        tempIndex = tempIndex + 1

    db.multi_modify(sql, resultTag)
    db.multi_modify(sql2, resultTag2)

    # 构造存入item_tag表数据
    print("---开始存入item_tag表")
    print("共: " + str(len(itemTagList)) + "条")
    print("重复数据 " + str(repeatItemTag) + "条")
    tempIndex = 0
    sql = "replace into item_tag ( id, itemid, tagid) values (%s, %s, %s)"
    sql2 = "update item_tag set `index` = %s where id = %s"
    for i in itemTagList:
        # print(itemTagList)
        if i['itemid'] == '2018052514371931752756' and i['tagid'] == "2018052514372050159427":
            print("ok")
        i['index'] = tempIndex
        tempList = (i['id'], i['itemid'], i['tagid'])
        resultItemTag.append(tempList)
        resultItemTag2.append((i['index'], i['id']))
        tempIndex = tempIndex + 1

    db.multi_modify(sql, resultItemTag)
    db.multi_modify(sql2, resultItemTag2)

    db.close()





'''
def saveResult(dList):
    itemList = []
    tagList = []
    itemTagList = []

    resultItem = []
    resultTag = []
    resultItemTag = []

    repeatItem = 0
    repeatTag = 0
    repeatItemTag = 0

    # 处理原始dList参数
    for d in dList:
        item = {}
        item['id'] = ""
        item['name'] = d['name']
        item['link'] = myfunc.ifNullValue(d['link'])
        item['root'] = myfunc.get_root(item['link'])
        item['updatetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item['tag'] = d['tag']
        # item['fromurl'] = d['fromurl']

        if item in itemList:
            itemList[itemList.index(item)]['tag'] + item['tag']
        else:
            itemList.append(item)

        tag = d['tag']

        tIndex = []

        # print(tag)
        if tag:
            tempTag = {}
            tempTag['fromurl'] = d['fromurl']

            for t in tag:
                if t not in tagList:
                    tempTag['id'] = ""
                    tempTag['name'] = t
                    tagList.tempTag(tempTag)
                tIndex.append(tagList.index(tempTag))

        itemTag = {**item, **{'index': tIndex}}
        # print(itemTag)
        itemTagList.append(itemTag)

    db = SQLManager.SQLManager()
    # 获取 itemId
    for i in itemList:
        sql = "select id from item where name = %s"
        args = i['name']
        result = db.get_one(sql, args)

        if result:
            repeatItem = repeatItem + 1
            itemTagList[itemList.index(i)]['itemid'] = itemList[itemList.index(i)]['id'] = result['id']
        else:
            itemTagList[itemList.index(i)]['itemid'] = itemList[itemList.index(i)]['id'] = myfunc.genid()
        # print(itemList)

    # 获取tagId

    for i in range(len(tagList)):
        sql = "select id from tag where name= %s"
        args = tagList[i]['name']
        result = db.get_one(sql, args)

        if result:
            repeatTag = repeatTag + 1
            itemTagList[i]['tagid'] = tagList[i]['id'] = result['id']
        else:
            itemTagList[i]['tagid'] = tagList[i]['id'] = myfunc.genid()
            itemTagList[i]['tagid'] = tagList[i]['id'] = myfunc.genid()


    # 获取itemTagId

    for i in range(len(itemTagList)):
        sql = "select id from item_tag where itemid = %s and tagid = %s"
        for m in itemTagList[i]['index']:
            args = (itemList[i]['id'], tagList[m]['id'])
            # print(args)
            result = db.get_one(sql, args)

            if result:
                repeatItemTag = repeatItemTag + 1
                itemTagList[i]['id'] = result['id']
            else:
                itemTagList[i]['id'] = myfunc.genid()




    print(len(itemList))
    for i in itemList:
        print(i)

    print(len(tagList))
    for i in tagList:
        print(i)

    print(len(itemTagList))
    for i in itemTagList:
        print(i)
    # 构造存入item表数据
    print("---开始存入item表")
    print("共: " + str(len(itemList)) + "条")
    print("重复数据 " + str(repeatItem) + "条")
    tempIndex = 0
    sql = "replace into item (id, `name`, link, root, updatetime, `index`) values(%s, %s, %s, %s, %s, %s)"
    for i in itemList:
        i['index'] = tempIndex
        tempList = (i['id'], i['name'], i['link'], i['root'], i['updatetime'], i['index'])

        resultItem.append(tempList)
        tempIndex = tempIndex + 1
        # print(tempList)



    # db.multi_modify(sql, resultItem)

    # 构造存入tag表数据
    print("---开始存入tag表")
    print("共: " + str(len(tagList)) + "条")
    print("重复数据 " + str(repeatTag) + "条")
    tempIndex = 0
    sql = "replace into tag (fromurl, id, `name`, `index`) values (%s, %s, %s, %s)"
    for i in tagList:
        i['index'] = tempIndex

        tempList = (i['fromurl'], i['id'], i['name'], i['index'] )
        resultTag.append(tempList)
        tempIndex = tempIndex + 1
        # print(tempList)

    # db.multi_modify(sql, resultTag)

    # 构造存入item_tag表数据
    print("---开始存入item_tag表")
    print("共: " + str(len(itemTagList)) + "条")
    print("重复数据 " + str(repeatItemTag) + "条")
    tempIndex = 0
    sql = "replace into item_tag ( id, itemid, tagid, `index`) values (%s, %s, %s, %s)"
    for i in itemTagList:
        i['index'] = tempIndex
        tempList = (i['id'], i['itemid'], i['tagid'], i['index'])
        resultItemTag.append(tempList)
        tempIndex = tempIndex + 1
        # print(tempList)

    # db.multi_modify(sql, resultItemTag)

    db.close()
    pass
'''

def saveResult_test(dList):
    db = SQLManager.SQLManager()
    for d in dList:
        sql = "select id from item where `name` = %s"
        args = d['name']
        result = db.get_one(sql, args)

        if not result:
            print("未找到item记录: ")
            print(d)
        else:
            itemid = result['id']

            # print("tag length: " + str(len(d['tag'])))
            for t in d['tag']:
                sql = "select id from tag where `name` = %s"
                args = t
                result = db.get_one(sql, args)

                if not result:
                    print("未找到tag记录: ")
                    print(t)
                else:
                    tagid = result['id']

                    sql = "select * from item_tag where itemid = %s and tagid = %s"
                    args = (itemid, tagid)

                    result = db.get_list(sql, args)
                    if len(result) == 0:
                        print("---------------------------------------未找到item_tag记录: ")
                        print(d)
                        print(t)






