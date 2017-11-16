import sqlite3
conn = sqlite3.connect('school.db')

print "Opened database successfully"
c = conn.cursor()

#create table
c.execute('''CREATE TABLE school
             (id INTEGER PRIMARY KEY AUTOINCREMENT not null,
             school_name text unique not null,
             user_name text not null,
             password text not null,
             path_file text,
             predict int)''')

print "Created table successs"

conn.close()

