import pysftp
import os


def put_mutiple(conn, arg):
    for i in arg:
        try:
            local_file = os.getcwd() + '/' + i
            conn.put(local_file)

        except:
            print('Error putting mutiple files onto remote')
