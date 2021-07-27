import pysftp
#import paramiko
from cwd import cwd


def cd(conn, args):

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
