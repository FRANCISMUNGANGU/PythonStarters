import sqlite3
# first we create the database
# create a variable to store your reference to the data connection
conn = sqlite3.connect("emobilis.db")
# to create a new table we use the command CREATE TABLE
# when defining headings include data types and any other extra information
# to make my table easy for relation models each table will have an id field or id column which is unique(PRIMARY KEY)
# PRIMARY KEYS: allow access to a specific record
conn.execute('''CREATE TABLE IF NOT EXISTS students(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
             );''')

conn.execute('''CREATE TABLE IF NOT EXISTS lecturers(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    staffnumber INTEGER NOT NULL
             );''')

# INSERTING RECORDS TO TABLE
# when inserting records use  prepared statements: prevents hacking through SQL (injection uses queston marks)
name = "Francis"
email = "francismungangu@gmail.com"
conn.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
conn.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Mary", "mary@gmail.com"))

# RETRIEVE DATA
# a variable to reference the fetch: so that you can list the loops data returned sql
cursor = conn.execute("SELECT * FROM students")
print(cursor)  # list of data from fetch
# cursor = conn.execute(SELECT * FROM USER)
# print data from user table
for row in cursor:
    print(f"id : {row[0]}, name : {row[1]}, email : {row[2]}")
# update data
conn.execute("UPDATE students SET name = ? WHERE id = ?", ("new name", 1))
# # delete data
conn.execute("DELETE FROM students WHERE id = ?", (2,))
# commit changes to database
conn.commit()
# close connection
conn.close()
