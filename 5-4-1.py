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
print(type(c))

#데이터베이스 생성
#c.execute('create database python_app2') #DDL,DML,DCL

#커서 반환
c.close()

#접속해제
conn.close()
