import sqlite3
from school import School

# chon 1 truong voi username
def select_school(username):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("SELECT * FROM school WHERE user_name = '%s'" % username)
    row = c.fetchone()
    school = School(id = row[0], name = row[1], username= row[2],password=row[3],filepath=row[4],predict=row[5])
    conn.close()
    return school

#column la ten cot muon update
def update_column(id,column,result):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("UPDATE school SET %s = ? WHERE id = ?" %(column) ,(result , id))
    print c.fetchone()
    conn.commit()
    conn.close()

# them 1 truong dai hoc
def insert_school(school):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("INSERT INTO school (school_name, user_name, password) VALUES (?, ?, ?)",
              (school.name, school.usename, school.password))
    print c.fetchone()
    conn.commit()
    conn.close()

# print select_school('hust').predict
# update_file(1,'predict',23)
# insert_school(school)
# school = School(id = None, name= 'Dai hoc xay dung', username='nuce', password='123')
