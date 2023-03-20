import sqlite3

from sqlite3 import Error

import datetime


def sql_connection():
    try:

        con = sqlite3.connect(':memory:')

        print("Connection is established: Database is created in memory")

        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, "
        "hireDate text)")

    con.commit()


def sql_insert(con, entities):
    cursorObj = con.cursor()

    cursorObj.execute(
        'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)

    con.commit()


def sql_update(con):
    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')

    con.commit()


def sql_fetch(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


def sql_fetch_tables(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())

def sql_fetch_with_condition(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)

def sql_insert_multy(con):
    cursorObj = con.cursor()

    cursorObj.execute('create table if not exists projects(id integer, name text)')

    data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]

    cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)
    con.commit()

def sql_table_not_exist(con):
    cursorObj = con.cursor()

    cursorObj.execute('create table if not exists projects(id integer, name text)')

    con.commit()

def sql_date(con):
    cursorObj = con.cursor()

    cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')

    data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]

    cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)

def sql_delete_table(con):
    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()






con = sql_connection()
sql_table(con)

entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

sql_insert(con, entities)
sql_update(con)
sql_fetch(con)
sql_fetch_with_condition(con)
sql_fetch_tables(con)
sql_table_not_exist(con)
sql_delete_table(con)
sql_insert_multy(con)

con.close()
