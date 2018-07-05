import sqlite3
from functools import wraps

def cursor(func):
    @wraps(func)
    def wrapper(self,*args, **kwargs):
        self.conn = sqlite3.connect(self.tablebase)
        self.cursor = self.conn.cursor()
        result = func(self,*args, **kwargs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
        return result
    return wrapper

class SQlite():
    def __init__(self,tablebase):
        self.tablebase = tablebase

    @cursor
    def create_table(self,tablename,**kw):
      header = ','.join(['{0} {1}'.format(key,kw[key]) for key in kw.keys()])
      sql = 'CREATE TABLE {tablename}({header})INTEGER PRIMARY KEY AUTOINCREMENT '.format(tablename = tablename,header = header)
      print(sql)
      self.cursor.execute(sql)

    @cursor
    def insert(self,tablename,**kw):
        header = ','.join(kw.keys())
        value = ','.join(["'{0}'".format(key) if isinstance(key,str) else str(key) for key in kw.values()])
        sql = "INSERT INTO {tablename} ({header}) VALUES ({value})".format(tablename = tablename,header = header,value = value)
        self.cursor.execute(sql)
        print(sql)

    def _select(self,tablename,*keys,where = ''):
        headers = ','.join(keys)
        sql = "SELECT {0} from {1} {2}".format(headers,tablename,where)
        result = self.cursor.execute(sql)
        return result
    @cursor
    def update(self):
        self.cursor.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    @cursor
    def delete(self):
        self.cursor.execute("DELETE from COMPANY where ID=2;")
    @cursor
    def fetchall(self,tablename,*keys,where = ''):
        result = self._select(tablename,*keys,where = where)
        return result.fetchall()
    @cursor
    def fetchone(self,tablename,*keys,where = ''):
        result = self._select(tablename,*keys,where = where)
        return result.fetchone()

def test():
  db = SQlite('helloy')
  # db.create_table('htmldata',ID = 'INTEGER PRIMARY KEY AUTOINCREMENT ',NAME = 'text')
  db.insert('htmldata',name = 'hello')
  result = db.fetchone('htmldata','id','name')
  result = db.fetchall('htmldata','id','name')
  print(result)

test()