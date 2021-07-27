import pysftp


def rename(conn, arg):

    arg_count = len(arg)

    if arg_count < 2:
        print("must include both names for file rename.")
        return

    new_name = arg[0]
    old_name = arg[1]

    try:
        conn.rename(new_name, old_name)

    except:
        print("Error renaming files.")
