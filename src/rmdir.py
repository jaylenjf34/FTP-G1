import pysftp


def rmdir(conn, args):

    arg_count = len(args)
    if arg_count < 1:
        print("Error, must include a directory to remove.")
        return

    filename = args[0]

    try:
        conn.rmdir(filename)

    except:
        print("Directory not found.")
