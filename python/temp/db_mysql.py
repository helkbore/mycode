import pymysql


host = 'localhost'
username = 'root'
password = 'root'
port = 3306
db_name = 'favorites'





def execute_save(sql):
    # print(sql)
    conn = pymysql.connect(
        host=host,
        user=username,
        port=port,
        password=password,
        db=db_name
    )

    conn.set_charset("utf8")


    cursor = conn.cursor()

    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')


    # print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    conn.commit()

    return result

def execute_insert(sql):
    # print(sql)
    conn = pymysql.connect(
        host=host,
        user=username,
        port=port,
        password=password,
        db=db_name
    )

    conn.set_charset("utf8")


    cursor = conn.cursor()

    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

    cursor.execute(sql)
    result = cursor.lastrowid

    return result

def save_item(d):
    # 判断名称是否已存在
    select_item_sql = "select * from item where name= '%s' " % (d['name'])
    result = execute_save(select_item_sql)

    if len(result) == 0:
        # add item
        value = "'" + d['name'] + "','" + d['root'] + "','" + d['link'] + "'"
        insert_item_sql = "insert into item (name, root, link) values ( %s )" % (value)

        # print(insert_item_sql)

        item_id = execute_insert(insert_item_sql)
    else:
        item_id = result[0][0]

    if 'tag' in d.keys():
        # select type
        select_type_sql = "select * from tag where name= '%s' " % (d['tag'])
        type_result = execute_save(select_type_sql)

        # print("--")
        # print(type_result)

        # add item_type
        if len(type_result) == 0:
            insert_type_sql = "insert into tag (name) values ( %s )" % ("'" + d['tag'] + "'")
            type_id = execute_insert(insert_type_sql)
        else:
            type_id = type_result[0][0]

            insert_itemType_sql = "insert into item_tag (itemid, tagid) values (%d, %d)" % (item_id, type_id)
            execute_insert(insert_itemType_sql)




# execute_save("select * from item where name= '快捷搜索' or root = 'http://pandecheng.ml'")
