import pymysql

#MySQL Connection
conn=pymysql.connect(host='localhost',user='M',password='1234',db='python_app1',charset='utf8')

try:
    with conn.cursor() as c: #conn.cursor(pymysql.cursors.DictCursor)
        c.execute("SELECT * FROM users")
        #1개 로우 지정
        #print(c.fetchone())
        #선택 지정
        #print(c.fetchmany(3))
        #전체 로우
        #print(c.fetchall())

        #순회1
        c.execute("SELECT * FROM users ORDER BY id ASC")
        rows=c.fetchall()
        for row in rows:
            print('usage1 > ',row)

        #순회2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('usage2 > ',row)

        #조건조회1
        param1=(1,)
        c.execute("SELECT * FROM users WHERE id=%s",param1)
        print('param1',c.fetchall())

        #조건조회2
        param2=1
        c.execute('SELECT * FROM users WHERE id="%d"'%param2) #python formatting : %s,%f,%d,%o,%x
        print('param2',c.fetchall())

        #조건조회3
        param3=(4,5)
        c.execute('SELECT * FROM users WHERE id IN(%s,%s)',param3)
        print('param3',c.fetchall())

        #조건조회4
        param4=(4,5)
        c.execute('SELECT * FROM users WHERE id IN("%d","%d")' % param4)
        print('param4',c.fetchall())



finally:
    conn.close()
