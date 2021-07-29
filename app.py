import pysftp
import getpass
from src import *
from log import log


def switch_statment(conn, arg):
    args = arg.split()
    cmd = args[0]
    args.pop(0)

    if(cmd == 'ls'):
        ls(conn, args)
    elif(cmd == "mkdir"):
        mkdir(conn, args)
    elif(cmd == 'rmdir'):
        rmdir(conn, args)
    elif(cmd == 'pwd' or cmd == 'cwd'):
        cwd(conn)
    elif(cmd == 'cd'):
        cd(conn, args)
    elif(cmd == 'rename'):
        rename(conn, args)
    elif(cmd == 'rm'):
        rm(conn, args)
    elif(cmd == 'put' and args_len < 2):
        put(conn, args)
    elif(cmd == 'put' and args_len >= 2):
        put_mutiple(conn, args)
    elif cmd == 'q' or cmd == 'logout' or cmd == 'exit':
        logout(conn)
    else:
        print("Command not found.")


def main():
    sftp = login()

    while True:
        line = input('$ ')
        log(line)
        switch_statment(sftp, line)


if __name__ == "__main__":
    main()
