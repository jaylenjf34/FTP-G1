import pysftp
import getpass
from longlist import ls
from login import login


def switch_statment(conn, arg):
    args = arg.split()
    cmd = args[0]
    args.pop(0)

    if(cmd == 'ls'):
        ls(conn, args)
    elif(cmd == "mkdir"):
        try:
            conn.mkdir(args[1])
        except:
            print("Directory already exists or not specified")
    elif(cmd == 'rmdir'):
        try:
            conn.rmdir(args[1])
        except:
            print("Directory not found")
    elif(cmd == 'pwd'):
        my_pwd = conn.pwd
        print(my_pwd)
    elif(cmd == 'cd'):
        try:
            if(args[1] == '..'):
                path = conn.pwd()
                my_path = conn.path_retreat(path)
                my_cd = conn.cwd(my_path[1])
                print("HELP")
            else:
                my_cd = conn.cwd(args[1])
            print(args[1])
        except:
            print("Directory not found")

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
