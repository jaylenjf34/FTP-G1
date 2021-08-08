import pysftp


def mkdir(conn, args):

    filename = args[0]

    try:
        conn.mkdir(filename)

    except:
        print("Directory already exists or not specified.")
        return -1
