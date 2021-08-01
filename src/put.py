import pysftp
import os

def put(conn, arg):

    print(os.getcwd())
    local_file = os.getcwd() + '/' + arg[0]
    remote_path = conn.pwd
    try:
        conn.put(local_file)

    except:
        print('Could not put local file on remote')
