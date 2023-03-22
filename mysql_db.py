import pymysql
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')
# the configuration message for mysql server
host = config['mysql']['host']
port = config['mysql']['port']
user = config['mysql']['user']
password = config['mysql']['password']
database = config['mysql']['database']

# table name
tablename = 't_account'

# columns one list in db
columns1 = "info, nickname, account, password, website, bind_email, bind_phone, `create_time`, `update_time`, comment"
# columns two list in db
columns2 = "id, " + columns1
# columns three list in db
columns3 = "info, nickname, account, password, website, bind_email, bind_phone, comment"


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
                VALUES('{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}');
    """.format(tablename, columns3,
               account['info'], account['nickname'], account['account'], account['password'],
               account['website'], account['bind_email'], account['bind_phone'], account['comment'])
    sql = sql.replace("'None'", "null")
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

    eneity = selectById(account['id'])[0]
    import datetime
    account['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") if eneity['password'] != account['password'] else eneity['update_time']

    # SQL 更新语句
    sql = """ update {} 
    set info = '{}',nickname= '{}', account='{}', password='{}', website='{}', bind_email='{}', bind_phone= '{}', update_time='{}', comment='{}'
    where id  = {}
    """.format(tablename,
               account['info'], account['nickname'], account['account'], account['password'],
               account['website'], account['bind_email'], account['bind_phone'], account['update_time'], account['comment'],
               account['id'])
    sql = sql.replace("'None'", "null")
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()

def selectPage(limit, offset, q=''):
    sql = """SELECT {}
        FROM {} where info like '%{}%' or comment like '%{}%'
        limit {}, {}""".format(columns2, tablename, q, q, limit, offset)
    return executeSelectSql(sql)

def count(q=''):
    sql = """select count(1)
    FROM {} where info like '%{}%' or comment like '%{}%'
    """.format(tablename, q, q)
    print(sql)
    conn = connect();
    conn.ping(reconnect=True)
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()
    return int(results[0][0])

def selectAll():
    sql = """SELECT {}
        FROM {}
        """.format(columns2, tablename)
    return executeSelectSql(sql)
def selectById(id):
    sql = """SELECT {}
        FROM {} 
        where id = {}
        """.format(columns2, tablename, id)
    return executeSelectSql(sql)

# 执行查询的 sql
def executeSelectSql(sql):
    print(sql)
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
            'bind_email': str(i[6]),
            'bind_phone': str(i[7]),
            'create_time': str(i[8]),
            'update_time': str(i[9]),
            'comment': str(i[10])
        })
    cursor.close()
    conn.close()

    return resultsList


def deleteById(id):
    conn = connect()
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