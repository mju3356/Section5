import pymysql
import simplejson
import datetime

#MySQL Connection
conn=pymysql.connect(host='localhost',user='M',password='1234',
                   db='python_app1',charset='utf8')
#pyMySQL 버전확인
#print('pymysql.version',pymysql.__version__)

#데이터베이스 선택
#conn.select_db('python_app1')

#cursor 연결
c=conn.cursor()
#print(type(c))

#데이터베이스 생성
#c.execute('create database python_app2') #DDL,DML,DCL

#커서 반환
#c.close()

#접속해제
#conn.close()

#트랜잭션 시작 선언
#conn.begin()

#커밋
#conn.commit()

#롤백
#conn.rollback()

#날짜 생성
now=datetime.datetime.now()
nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

#테이블 생성
c.execute('CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL,\
                        username varchar(20),\
                        email varchar(30),\
                        phone varchar(30),\
                        website varchar(30),\
                        regdate varchar(20) NOT NULL, PRIMARY KEY(id))')
                        #AUTO_INCREMENT,DEFAULT
try:
    with conn.cursor() as c:
        #JSON to MySQL
        with open('c:/PythonApp/Section5/data/users.json','r') as infile:
            r=simplejson.load(infile)
            userData=[]
            for user in r:
                t=(user['id'],user['username'],user['email'],user['phone'],user['website'],nowDatetime)
                userData.append(t)
            c.executemany('INSERT INTO users(id,username,email,phone,website,regdate) VALUES (%s,%s,%s,%s,%s,%s)',userData)
        conn.commit()
finally:
    conn.close()
