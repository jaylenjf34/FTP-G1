import pysftp
import os
from termcolor import colored
from .cwd import cwd


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

    print("")
    print("=== Directories ===")

    for direc in direct:
        print(colored(direc, 'blue'))

    print("===================")
    print("")
    print("====== Files ======")

    for file in files:
        print(colored(file, 'magenta'))

    print("===================")

    # for directory in direct:
    #    print(directory)


def ls(conn, args):
    dir = '.'
    if args:
        dir = args[0]

    print_formatted(format_dir(conn.listdir(remotepath=dir)))
