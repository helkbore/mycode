import pymysql


DB_CONFIG = {
    "host"     : 'localhost',
    "port"     : 3306,
    "user" :'root',
    "password" : "root",
    "db"  : 'fav',
    "charset"  : "utf8"

}

class SQLManager(object):
    # 初始化
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(
            host = DB_CONFIG['host'],
            port = DB_CONFIG['port'],
            user = DB_CONFIG['user'],
            password = DB_CONFIG['password'],
            db = DB_CONFIG['db'],
            charset = DB_CONFIG['charset']
        )

        self.cursor = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    # 查询多条数据
    def get_list(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            result = self.cursor.fetchall()
            return result
        except BaseException as e:
            print("---------------error----------------")
            print("error: ", e)
            print(sql)


    # 查询单条
    def get_one(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result
        except BaseException as e:
            print("---------------error----------------")
            print("error: ", e)
            print(sql)

    # 执行单条SQL语句
    def moddify(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except BaseException as e:
            print("---------------error----------------")
            print("error: ", e)
            print(sql)

    # 执行多条数据
    def multi_modify(self, sql, args=None):
        try:
            self.cursor.executemany(sql, args)
            self.conn.commit()
        except BaseException as e:
            print("---------------error----------------")
            print("error: ", e)
            print(sql)

    # 插入单条
    def create(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()
        last_id = self.cursor.lastrowid
        return last_id

    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.conn.close()
