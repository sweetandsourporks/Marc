import sqlite3

#connect to database
connection = sqlite3.connect('students.db')

#cursor
c = connection.cursor()





#ORDER THEM IN LIST
c.execute("SELECT rowid, * FROM students ORDER BY rowid")
items = c.fetchall()
for item in items:
    print(item)





#commit the command
connection.commit()

#close connection
connection.close()