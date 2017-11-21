import sqlite3

conn = sqlite3.connect('school.db')
print "Opened database successfully"
c = conn.cursor()

try:
        r = c.execute("INSERT INTO school (school_name, user_name, password) \
                  VALUES ('Dai hoc Nong Nghiep', 'hanu', '123' )")
        print "Insert success"
except sqlite3.Error as e :
        print e
conn.commit()

for row in conn.execute('SELECT * FROM school'):
        print row

# username = 'tbu'
# row = c.execute("SELECT * FROM school WHERE user_name = '%s'" % username)

# f = c.fetchone()
# print f[1]
conn.close()