import pysftp
import os


def logout(conn):
    conn.close()
    print("Connection to host closed. Returning control!")
    os.sys.exit()
