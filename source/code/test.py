def run_sql(cmd):
    import pymysql
    db = pymysql.connect("localhost","root","","test" )
    cursor = db.cursor()
    cursor.execute(cmd)
    data = cursor.fetchone()
    db.close()
    return data
cmd = "SELECT uname,upwd FROM mail163s"
data = run_sql(cmd)
print(data)