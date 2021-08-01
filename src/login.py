import pysftp
import getpass
import sys
import os
from termcolor import colored
import datetime
from save_connection import save_connect
from retrieve_connect import retrieve_connect


def login():
    # added for save Connection
    print('Do you want to connect to last host?')
    ans = input('Y/N ')

    if ans == 'N' or ans == 'n':
        SFTP_NET = input('Please enter the hostname: ')
        save_connect(SFTP_NET)

    else:
        SFTP_NET = retrieve_connect()

    SFTP_USER = input('Please enter your username: ')
    SFTP_PSWD = getpass.getpass()

    #SFTP_NET = 'linux.cs.pdx.edu'
    #SFTP_USER = 'keca2'
    #SFTP_PSWD = ''

    print("")
    print('Attempting connection to ' + colored(SFTP_NET, 'blue') +
          ' with user ' + colored(SFTP_USER, 'green') + '...')
    print("")

    try:
        log = open(os.path.expanduser('logfile.txt'), 'a')
        log.write('User ' + SFTP_USER + ' logged in at: ' +
                  datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S") + '\n')
        log.write('********************************************\n')
        log.close()

        sftp = pysftp.Connection(
            SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)

        print("Connection successful!")
        welcome = colored('Slightly Worse SFTP Application',
                          'cyan', attrs=['blink', 'bold'])
        print("")
        print("*** Welcome to ", end="")
        print(colored(welcome), end="")
        print("! ***")
        print("")

        return sftp

    except pysftp.AuthenticationException:
        print("Username " + colored(SFTP_USER, 'red') +
              " could not be authenticated. Exiting.")
        sys.exit()

    except pysftp.SSHException:
        print("Host: " + colored(SFTP_NET, 'red') +
              " could not be validated. Exiting.")
        sys.exit()

    else:
        print("Connection to host unsuccessful. Exiting")
