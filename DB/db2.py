
import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('town.db')

        return con

    except Error:

        print(Error)


def sql_table_create(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE if not exists streets(id integer PRIMARY KEY NOT NULL, name text)")

    con.commit()


def sql_insert_data(con):
    cursorObj = con.cursor()

    data = [(1, 'Гоголя'), (2, "Преображенского"), (3, "Первомайская"), (4, "Текстильшиков"), (5, "Щетинина")]

    cursorObj.executemany("INSERT INTO streets VALUES(?,?)", data)


def sql_select(con):
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM streets')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


con = sql_connection()
sql_table_create(con)
sql_insert_data(con)
sql_select(con)
con.close()