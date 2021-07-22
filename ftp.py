import ftplib
from getpass import getpass

def terminal() :

    print('Please enter login info for ftp')
    user_in = input('Enter User ')
    print('Enter Password ')
    password_in = getpass()
    host_in = input('Enter Host ')
    ftp = ftplib.FTP(host_in)
    ftp.login(user_in, password_in)
    ftp.pwd()
    line = input('$')




terminal()
