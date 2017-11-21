import sqlite3
from school import School

# chon 1 truong voi username
def select_school(username):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("SELECT * FROM school WHERE user_name = '%s'" % username)
    row = c.fetchone()
    if row is None:
        return None
    else:
        school = School(id=row[0], name=row[1], username=row[2], password=row[3], filepath=row[4], predict=row[5])
    conn.close()
    return school

#column la ten cot muon update path_file hoac predict
def update_column(username,column,result):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("UPDATE school SET %s = ? WHERE user_name = ?" %(column) ,(result , username))
    print c.fetchone()
    conn.commit()
    conn.close()

# them 1 truong dai hoc
def insert_school(school):
    conn = sqlite3.connect('school.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO school (school_name, user_name, password) VALUES (?, ?, ?)",
                  (school.name, school.username, school.password))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print "Error:", e
        return False

    conn.close()

# print select_school('hust').predict
# update_file(1,'predict',23)
# insert_school(school)
# school = School(id = None, name= 'Dai hoc xay dung', username='nuce', password='123')
