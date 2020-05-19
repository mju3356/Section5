import sqlite3
import urllib.request
import simplejson

con1=sqlite3.connect('c:/PythonApp/Section5/databases/0519homrwork.db')
c1=con1.cursor()

c1.execute('CREATE TABLE IF NOT EXISTS post(userid integer, id numeric PRIMARY KEY,title text,body text )')
c1.execute('CREATE TABLE IF NOT EXISTS comment(userid integer,id numeric PRIMARY KEY,name text,email text,body text)')

post=simplejson.loads(urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts').read())
comment=simplejson.loads(urllib.request.urlopen('https://jsonplaceholder.typicode.com/comments').read())
ud1=[]
ud2=[]

for u in post:
    t=(u['userId'],u['id'],u['title'],u['body'])
    ud1.append(t)
for u in comment:
    t=(u['postId'],u['id'],u['name'],u['email'],u['body'])
    ud2.append(t)

#c1.executemany('INSERT INTO post(userid,id,title,body) VALUES(?,?,?,?)',ud1)
#c1.executemany('INSERT INTO comment(userid,id,name,email,body) VALUES(?,?,?,?,?)',ud2)

#print(con1.execute('DELETE FROM post').rowcount)
#print(con1.execute('DELETE FROM comment').rowcount)


print(c1.execute("SELECT * FROM post INNER JOIN comment").fetchall())


con1.commit()
con1.close()
