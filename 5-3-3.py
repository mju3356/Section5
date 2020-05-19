import sqlite3

#DB생성
conn=sqlite3.connect('c:/PythonApp/Section5/databases/sqlite1.db')

#커서 연결
c=conn.cursor()

#데이터 수정
c.execute('UPDATE users SET username=? WHERE id=?',('niceman',1))

#데이터 수정2
c.execute('UPDATE users SET username=:name WHERE id=:id',{'name':'goodboy','id':2})

#데이터 수정3
c.execute("UPDATE users SET username='%s' WHERE id='%s'"%('cuteboy',3))

#데이터 제거
c.execute("DELETE FROM users WHERE id=?",(1,))

#데이터 제거2
c.execute("DELETE FROM users WHERE id=:id",{'id':2})

#데이터 제거3
c.execute("DELETE FROM users WHERE id='%s'"%3)

#중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

conn.commit()
conn.close()
