import pysftp
import getpass
from longlist import ls
from login import login
from changedir import cd


def switch_statment(conn, arg):
    args = arg.split()
    cmd = args[0]
    args.pop(0)

    if(cmd == 'ls'):
        ls(conn, args)
    elif(cmd == "mkdir"):
        try:
            conn.mkdir(args[0])
        except:
            print("Directory already exists or not specified")
    elif(cmd == 'rmdir'):
        try:
            conn.rmdir(args[0])
        except:
            print("Directory not found")
    elif(cmd == 'pwd' or cmd == 'cwd'):
        cwd(conn)
    elif(cmd == 'cd'):
        cd(conn, args)

    else:
        print("Command not found")


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
