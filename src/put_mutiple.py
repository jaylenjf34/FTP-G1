import pysftp
from src.put import put


def put_mutiple(conn, arg):
    for i in arg:
        try:
            put(conn, i)

        except:
            print('Error putting mutiple files onto remote')
