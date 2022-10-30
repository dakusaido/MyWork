import sqlite3


def save_log_pas(path: str, login: str, password):
    if login.isdigit():
        raise "Login not be int"

    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS person(log TEXT, password TEXT)""")

    cursor.execute("""SELECT * FROM person""")
    if login in (x[0] for x in cursor.fetchall()):
        return False

    cursor.execute("""INSERT INTO person VALUES(?, ?)""", (login, password))
    conn.commit()


if __name__ == '__main__':
    save_log_pas('test.db', 'Fedya', 12345)
