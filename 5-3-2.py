import sqlite3

#DB생성
conn=sqlite3.connect('c:/PythonApp/Section5/databases/sqlite1.db')

#커서 바인딩
c=conn.cursor()

#데이터 조회
c.execute("SELECT * FROM users")

#1개 로우 선택
#print(c.fetchone())

#지정 로우 선택
#print(c.fetchmany(size=4))

#전체 로우 선택
#print(c.fetchall())

#순회1
#rows=c.fetchall()
#for r in rows:
    #print('usage1>',r)

#순회2
#for row in c.fetchall():
    #print('usage2>',row)

#순회3
#for row in c.execute('SELECT * FROM users'):
#    print('usage3',row)


#조건 조회
param1=(1,)
c.execute('SELECT * FROM users WHERE id=?',param1)
print(c.fetchall())

#조건 조회2
param2=1
c.execute("SELECT * FROM users WHERE id='%s'"%param2) #%s %d %f %x %o
print(c.fetchall())

#조건 조회3
c.execute('SELECT * FROM users WHERE id=:id',{'id':1})
print(c.fetchall())

#조건 조회4
param4=(1,4)
c.execute("SELECT * FROM users WHERE id IN(?,?)",param4)
print(c.fetchall())

#조건 조회5
c.execute('SELECT * FROM users WHERE id=:id1 OR id=:id2',{'id1':1,'id2':2})
print(c.fetchall())

#조건 조회6
param2=1,3
c.execute("SELECT * FROM users WHERE id='%s' OR id='%s'"%param2) #%s %d %f %x %o
print(c.fetchall())

#dump
with conn:
    #dump출력
    with open('c:/PythonApp/Section5/data/test.dump','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line )
        print('Dump Write Complete!')
