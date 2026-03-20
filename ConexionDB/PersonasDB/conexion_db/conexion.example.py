import mysql.connector


def conecta_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="name_db"
    )
