import pysftp


def get(conn, arg):
    if len(arg) < 1:
        print('Please specify a file name to get onto local.')
        return

    remote_file = conn.pwd + '/' + arg[0]

    try:
        return conn.get(remote_file)
    except:
        print('Could not get the file.')
        return -1
