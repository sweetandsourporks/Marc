import sqlite3

#connect to database
connection = sqlite3.connect('admins.db')

#cursor
c = connection.cursor()







#place execute files here









#commit the command
connection.commit()

#close connection
connection.close()
