import sqlite3
db=sqlite3.connect("insert.db")
cr=db.cursor()
cr.execute("create table ins(Roll text,Name text,Father Name text,Contact No text)")
db.commit()
db.close()
print("table create")