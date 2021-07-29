import pysftp

def put(conn, arg):

    local_file = arg[0]
    remote_path = conn.pwd
    try:
        conn.put(local_file, remote_path)

    except:
        print('Could not put local file on remote')
