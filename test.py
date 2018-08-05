import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\test\Desktop\test.accdb;')
cursor=conn.cursor()
cursor.execute('select * from table1')

for row in cursor.fetchall():
    print(row)

