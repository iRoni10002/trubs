# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('mydatabase.db')
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (name varchar, password int)''')
admin = [('dima', '123')]
cursor.executemany("INSERT INTO users VALUES (?,?)", admin)
conn.commit()
cursor.execute("SELECT * FROM users")
x = cursor.fetchall()
y = x[0]
print(y[1])

cursor.execute('''CREATE TABLE city (name varchar)''')
jj = str("gg")
city = [jj]
cursor.execute("INSERT INTO city VALUES (?)", city)
jj = str("gh")
city = [jj]
cursor.execute("INSERT INTO city VALUES (?)", city)
city = ['pa']
cursor.execute("INSERT INTO city VALUES (?)", city)
conn.commit()
cursor.execute("SELECT * FROM city")
x = cursor.fetchall()
y = x[0]
print(y[0])

cursor.execute('''CREATE TABLE units (brand varchar, type varchar, station_number varchar, reg_number varchar)''')
unit = [('xiaomi', 'котел', '2D4', '2D1')]
cursor.executemany("INSERT INTO units VALUES (?,?,?,?)", unit)
cursor.execute("SELECT * FROM units")
x = cursor.fetchall()
print(x[0])
cursor.close()
conn.close()
