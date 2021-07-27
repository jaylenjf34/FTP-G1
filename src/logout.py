import pysftp


def logout(conn):
    conn.close()
    print("Connection to host closed. Returning control!")
