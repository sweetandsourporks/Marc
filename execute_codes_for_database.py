#CREATE TABLE AND LISTS WITHIN IT
c.execute("""CREATE TABLE admins (
        first_name text,
	last_name text,
	email text,
	contact_number text
    )""")

#INSERT VALUES
c.execute("INSERT INTO admins VALUES ('Marc Justin Lee', 'Granada', 'granadamarc96@gmail.com', '09760333726')")

#LIST DOWN IN ROWS
c.execute("SELECT rowid, * FROM admins ORDER BY rowid")
items = c.fetchall()
for item in items:
    print(item)

#DELETE VALUES
c.execute("DELETE from admins WHERE rowid = 2")


#place 
print("code works") 
#after every execute code to know whether the code worked or not except in "list down in rows" because it already has a print func

#PROFESSORS values 
#first_name text,
#last_name text,
#email text,
#contact_number text
#subject text,
#schedule text,

#STUDENTS values
#first_name text,
#last_name text
#email text,

#ADMINS values
#first_name text,
#last_name text,
#email text,
#contact_number text
