import pysftp
import getpass

def switch_statment (conn, arg):
    if(arg == 'ls'):
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
        line = input('$')
        switch_statment(sftp, line)
        if(line == 'logout'):
            break;



if __name__ == "__main__":
    main()
