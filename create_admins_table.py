import sqlite3

#connect to database
connection = sqlite3.connect('admins.db')

#cursor
c = connection.cursor()

#create a table
c.execute("""CREATE TABLE admins (
        email text,
        first_name text,
        last_name text,
        contact_number text
    )""")


#commit the command
connection.commit()

#close connection
connection.close()
