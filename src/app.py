import pysftp
import getpass
from longlist import ls
from login import login
from changedir import cd
from cwd import cwd
from mkdir import mkdir
from rmdir import rmdir
from rename import rename
from rm import rm
from logout import logout


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
    elif cmd == 'q' or cmd == 'logout' or cmd == 'exit':
        logout(conn)
    else:
        print("Command not found.")


def main():
    sftp = login()

    while True:
        line = input('$ ')
        if(line != 'logout' or line != 'q'):
            switch_statment(sftp, line)
        if(line == 'logout' or line == 'q'):
            sftp.close()
            break


if __name__ == "__main__":
    main()
