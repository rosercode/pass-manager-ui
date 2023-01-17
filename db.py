import pymysql

# the configuration message for mysql server
host = '10.0.8.11'
port = 3308
user = 'root'
password = '123456'

# datanase name
database = 'account_db'

# table name
tablename = 'account'

# columns one list in db
columns1 = "info, nickname, account, password, website, bind_email, bind_phone, `create_time`, `update_time`, comment"
# columns two list in db
columns2 = "id, " + columns1

def connect():
    return pymysql.connect(host=host,
                           port=port,
                           user=user,
                           password=password,
                           database=database)

def insert(account):
    conn = connect();
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql = """INSERT INTO {0} ({1}) 
                VALUES('{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}');
    """.format(tablename, columns1,
               account['info'], account['nickname'], account['account'], account['password'],
               account['website'], account['bind_email'], account['bind_phone'], account['create_time'], account['update_time'], account['comment'])
    sql = sql.replace("'None'","null")
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 如果发生错误则回滚
        conn.rollback()

def update(account):
    conn = connect();
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    # SQL 更新语句
    sql = """ update {} 
    set info = '{}',nickname= '{}', account='{}', password='{}', website='{}', bind_email='{}', bind_phone= '{}', create_time='{}', update_time='{}', comment='{}'
    where id  = {}
    """.format(tablename,
               account['info'], account['nickname'], account['account'], account['password'],
               account['website'], account['bind_email'], account['bind_phone'], account['create_time'], account['update_time'], account['comment'],

               account['id'])
    sql = sql.replace("'None'","null")
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()

def selectPage(limit, offset):
    sql = """SELECT {}
        FROM {}
        limit {}, {}""".format(columns2, tablename,limit, offset)
    return executeSelectSql(sql)

def count():
    pass

def selectAll():
    sql = """SELECT {}
        FROM {}
        """.format(columns2, tablename)
    return executeSelectSql(sql)

# 执行查询的 sql
def executeSelectSql(sql):
    conn = connect();
    conn.ping(reconnect=True)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()
    resultsList = []
    for i in results:
        resultsList.append({
            'id': str(i[0]),
            'info': str(i[1]),
            'nickname': str(i[2]),
            'account': str(i[3]),
            'password': str(i[4]),
            'website': str(i[5]),
            'email': str(i[6]),
            'phone': str(i[7]),
            'create_time': str(i[8]),
            'update_time': str(i[9]),
            'comment': str(i[10])
        })
    cursor.close()
    conn.close()

    return resultsList


def deleteById(id):
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql = "DELETE FROM %s WHERE id = %d" % (tablename, id)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()