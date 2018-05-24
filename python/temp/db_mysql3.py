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

def getAllItem():
    db = SQLManager.SQLManager()
    result = db.get_list("select * from item")
    db.close()
    return result

def updateItemsSite(idList):
    sql = "update item set isSite = 1 where id = %s"
    args = idList
    db = SQLManager.SQLManager()
    db.multi_modify(sql, args)
    db.close()