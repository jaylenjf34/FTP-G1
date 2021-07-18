import ftplib
from getpass import getpass

def terminal() :

    print('Please enter login info for ftp')
    user = input('Enter User ')
    print('Enter Password ')
    password = getpass()
    host = input('Enter Host ')

    print(password)
    ftp = ftplib.FTP.login(user, host, password)
    line = input('$')

terminal()
