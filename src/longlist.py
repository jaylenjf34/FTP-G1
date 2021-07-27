import pysftp
import os


def format_dir(dir):
    formatted = dir
    for item in formatted[:]:
        if item.startswith('.'):
            formatted.remove(item)

    return formatted


def print_formatted(dir):
    files = []
    direct = []
    misc = []
    for item in dir:
        if "." in item:
            files.append(item)
        else:
            direct.append(item)

    print("=== Directories ===")

    for direc in direct:
        print(direc)

    print("==================")
    print("")
    print("===== Files ======")

    for file in files:
        print(file)

    print("=================")

    # for directory in direct:
    #    print(directory)


def ls(conn, args):
    if not args:
        print_formatted(format_dir(conn.listdir(remotepath='.')))

    else:
        dir = args[0]
