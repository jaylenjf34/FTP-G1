import pysftp


def rm(conn, args):
    arg_len = len(args)

    if arg_len < 1:
        print("Must include filename to delete.")
        return

    file_to_del = args[0]

    try:
        conn.remove(file_to_del)

    except:
        print("Error deleting the file.")
        return -1
