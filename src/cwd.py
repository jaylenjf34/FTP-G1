import pysftp


def cwd(conn):
    cwd = conn.pwd
    print(cwd)
    return cwd
