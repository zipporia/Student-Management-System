import sqlite3


def std_data():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,  std_id text, std_name text, std_surname text, std_dob text, \
                std_age text, std_gender text, std_address text, std_mobile text)")
    con.commit()
    con.close()


def add_std_rec(std_id, std_name, std_surname, std_dob, std_age, std_gender, std_address, std_mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",\
                (std_id, std_name, std_surname, std_dob, std_age, std_gender, std_address, std_mobile))
    con.commit()
    con.close()


def view_data():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows


def delete_rec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()


def search_data(std_id="", std_name="", std_surname="", std_dob="", std_age="", std_gender="", std_address="", std_mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE std_id=? or std_name=? OR std_surname=? OR std_dob=? OR \
                std_age=? OR std_gender=? OR std_address=? OR std_mobile=?", (std_id, std_name, std_surname, std_dob, std_age, std_gender, std_address, std_mobile))
    rows = cur.fetchall()
    con.close()
    return rows


def data_update(id, std_id="", std_name="", std_surname="", std_dob="", std_age="", std_gender="", std_address="", std_mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET std_id=?, std_name=?, std_surname=?, std_dob=?, std_age=?, std_gender=?, std_address=?, std_mobile=?",\
                (std_id, std_name, std_surname, std_dob, std_age, std_gender, std_address, std_mobile, id))
    con.commit()
    con.close()


std_data()
