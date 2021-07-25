import pysftp
import getpass

def switch_statment (conn, arg):
    args = arg.split()
    if(args[0] == 'ls'):
        my_ls = conn.listdir()
        print(my_ls)
    elif(args[0] == "mkdir"):
        try:
            conn.mkdir(args[1])
        except:
            print("Directory already exists or not specified")
    elif(args[0] == 'rmdir'):
        try:
            conn.rmdir(args[1])
        except:
            print("Directory not found")
    elif(args[0] == 'pwd'):
        my_pwd = conn.pwd
        print(my_pwd)
    elif(args[0] == 'cd'):
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
    SFPT_URL = 'linux.cs.pdx.edu'
    SFTP_NET = input('Please enter host: ')
    SFPT_USER = input('Please enter your username: ')
    SFPT_PSWD = getpass.getpass()
    sftp = pysftp.Connection(SFTP_NET, username=SFPT_USER, password=SFPT_PSWD)
    print('Attepting connection to ' + SFPT_URL + '...')
    while True:
        line = input('$ ')
        if(line != 'logout'):
            switch_statment(sftp, line)
        if(line == 'logout'):
            sftp.close()
            break;



if __name__ == "__main__":
    main()
