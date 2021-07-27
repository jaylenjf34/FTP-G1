import pysftp


def logout(conn):
    conn.close()
