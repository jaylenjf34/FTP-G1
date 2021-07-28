import pysftp
# import paramiko
from src.cwd import cwd
from termcolor import colored


def cd(conn, args):

    arg_count = len(args)

    if (arg_count == 0):
        print("Need directory to change into")
        return
 
    path = args[0]

    if(path == '..'):
        path.rsplit('/', 1)[0]
        conn.chdir(path)

    else:
        try:
            conn.chdir(path)

        except FileNotFoundError:
            print("No such directory located in current path.")

        # except paraminko.SFTPError:
        #    print("Desired path is not a directory.")

    print(colored('Moved to -> ', 'green'), end='')
    cwd(conn)
