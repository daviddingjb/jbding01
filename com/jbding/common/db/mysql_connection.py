import pymysql

# Function return a connection.
def getConnection():
    # You can change the connection arguments.
    conn = pymysql.connect(host='10.35.22.91',
                                 user='root',
                                 password='adminadmin',
                                 db='crawler')

    conn.set_charset('utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

    return conn,cursor

def getConnection(host, user, pwd, db):
    # You can change the connection arguments.
    conn = pymysql.connect(host=host, user=user, password=pwd, db=db)

    conn.set_charset('utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

    return conn,cursor
