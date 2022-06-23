import psycopg2 as psql
import sqlite3
import mysql.connector
import time


connPsql=psql.connect(user='user1',
                      password='123123',
                      host='localhost',
                      database='family')
curPsql=connPsql.cursor()
connMysql=mysql.connector.connect(user='jack',
                                  password='153351',
                                  host='localhost',
                                  database='jack_home'
                                  )
curMysql=connMysql.cursor()
connSqlite=sqlite3.connect('family.db')
curSqlite=connSqlite.cursor()
curSqlite.execute("""GREAT TABLE IF NOT EXISTS people(
                                   id INT,
                                   firstname TEXT,
                                   secondname TEXT""")
connSqlite.commit()
t1=time.time()
curPsql.execute('SELECT * FROM peoples')
a=curPsql.fetchall()
time1=time.time()-t1
print(a)
print(f'Время выгрузки из PostgreSQL : {time1}')
for i in a:
    curMysql.execute(f'INSERT INT0 people VALUES {i}'
connMysql.commit()
for i in a:
    curSqlite.execute(f'INSERT INTO people VALUES {i}')
connSqlite.commit()
t2=time.time()
curMysql.execute("SELECT * FROM people")
b=curMysql.fetchall()
time2=time.time()-t2
print(b)
print(f' Время выгрузки из MySQL: {time2}')
t3=time.time()
curSqlite.execute("SELECT * FROM people")
c=curSqlite.fetchall()
time3=time.time()-t3
print(c)
print (f' Время выгрузки из SQLite: {time3}')

