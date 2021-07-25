import pysftp
import getpass

def switch_statment (conn, arg):
    args = arg.split()
    if(args[0] == 'ls'):
        my_ls = conn.listdir()
        print(my_ls)

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
