import sqlite3

#connect to database
connection = sqlite3.connect('professors.db')

#cursor
c = connection.cursor()




c.execute("SELECT rowid, * FROM professors ORDER BY rowid")
items = c.fetchall()
for item in items:
    print(item)






#commit the command
connection.commit()

#close connection
connection.close()