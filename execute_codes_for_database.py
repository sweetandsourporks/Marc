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
