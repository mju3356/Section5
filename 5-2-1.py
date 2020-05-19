import simplejson
from tinydb.storages import MemoryStorage
from tinydb import TinyDB

#파일 DB 생성
db=TinyDB('c:/PythonApp/Section5/databases/database.db',default_table='users') #defult기본값=default

#메모리DB 생성
#db=TinyDB(storage=MemoryStorage,defau)

#테이블선택
users=db.table('users')
todos=db.table('todos')

#테이블 테이터 삽입
users.insert({'name':'kim','email':'test@google.com'})
todo.insert({'name':'homework','complete':False})
