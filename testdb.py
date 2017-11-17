import sqlite3

conn = sqlite3.connect('school.db')
print "Opened database successfully"
c = conn.cursor()
# conn.execute("INSERT INTO school (school_name, user_name, password) \
#               VALUES ('Dai hoc Ha Noi', 'hanu', '123' )")
# print "Insert success"
# conn.commit()

for row in conn.execute('SELECT * FROM school'):
        print row

username = 'tbu'
c.execute("SELECT * FROM school WHERE user_name = '%s'" % username)

f = c.fetchone()
print f[1]
conn.close()