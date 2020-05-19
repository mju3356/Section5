import sqlite3
import datetime
import simplejson

#DB생성
#conn=sqlite3.connect('c:/PythonApp/Section5/databases/sqlite1.db',isolation_level=None) #AutoCommit
conn=sqlite3.connect('c:/PythonApp/Section5/databases/sqlite1.db')
#메모리 DB생성
#conn=sqlite3.connect(':memory')

#날짜 생성
now=datetime.datetime.now()
print(now)

NowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
print(NowDatetime)

#sqlite3 버전확인
print('sqlite3.version',sqlite3.version)
print('sqllit3.sqlite_version',sqlite3.sqlite_version)

#Cursor 연결
c=conn.cursor()
print(type(c))

#테이블 생성(SQLite3 Datatype : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, email text,phone text, website text, regdate text)")#AUTOINCREMENT

#데이터 삽입
#c.execute("INSERT INTO users VALUES(1,'KIM','kim@naver.com','010-0000-0000','kim.co.kr',?)",(NowDatetime,))

userlist=(
    (2,'KIM','kim@naver.com','010-0000-0000','kim.co.kr',NowDatetime),
    (3,'KIM','kim@naver.com','010-0000-0000','kim.co.kr',NowDatetime),
    (4,'KIM','kim@naver.com','010-0000-0000','kim.co.kr',NowDatetime)
)
#c.executemany("INSERT INTO users(id,username,email,phone,website,regdate) VALUES(?,?,?,?,?,?)",userlist)

with open('c:/PythonApp/Section5/data/users.json','r') as infile:
    r=simplejson.load(infile)
    userData=[]
    for user in r:
        t=(user['id'],user['name'],user['email'],user['phone'],user['website'],NowDatetime)
        userData.append(t)
    #c.executemany("INSERT INTO users(id,username,email,phone,website,regdate) VALUES(?,?,?,?,?,?)",userData)

#테이블 삭제
#print('users db delete',conn.execute('delete from users').rowcount,'rows')
conn.commit()

conn.close()
