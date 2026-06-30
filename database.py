import sqlite3
def conn(): return sqlite3.connect("students.db")
def create_table():
 c=conn();c.execute("""CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,roll TEXT UNIQUE,department TEXT,year TEXT,email TEXT,phone TEXT)""");c.commit();c.close()
def add_student(n,r,d,y,e,p):
 c=conn();c.execute("INSERT INTO students(name,roll,department,year,email,phone) VALUES(?,?,?,?,?,?)",(n,r,d,y,e,p));c.commit();c.close()
def view_students():
 c=conn();rows=c.execute("SELECT * FROM students").fetchall();c.close();return rows
