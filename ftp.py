from ftplib import FTP
from getpass import getpass

def terminal() :

    print('Please enter login info for ftp')
    user = input('Enter User ')
    print('Enter Password ')
    password = getpass()
    host = input('Enter Host ')
    FTP.login(user, password, host)
    line = input('$')


terminal()
