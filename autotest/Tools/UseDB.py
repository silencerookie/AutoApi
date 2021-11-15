import pymysql

class MySQLHelper(object):
    conn = None

    # 构造函数
    def __init__(self, host, username, password, db, charset="utf8", port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.username,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset)
        # 创建游标
        self.cursor = self.conn.cursor()

    # 关闭数据库连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 查询一条记录
    def get_one(self, sql, params=()):
        ret = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            ret = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return ret

    # 查询所有记录
    def get_all(self, sql, params=()):
        list_data = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list_data = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list_data

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count
    # 插入
    def insert(self, sql, params=()):
        return self.__edit(sql, params)
    # 修改
    def update(self, sql, params=()):
        return self.__edit(sql, params)
    # 删除
    def delete(self, sql, params=()):
        return self.__edit(sql, params)