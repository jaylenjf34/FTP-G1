import pysftp
import getpass
import sys
from termcolor import colored


def login():
    SFTP_NET = input('Please enter the hostname: ')
    SFTP_USER = input('Please enter your username: ')
    SFTP_PSWD = getpass.getpass()

    #SFTP_NET = 'linux.cs.pdx.edu'
    #SFTP_USER = 'keca2'
    #SFTP_PSWD = ''

    print("")
    print('Attempting connection to ' + SFTP_NET +
          ' with user ' + SFTP_USER + '...')
    print("")

    try:
        sftp = pysftp.Connection(
            SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)

        print("Connection successful!")
        welcome = colored('Slightly Worse SFTP Application',
                          'cyan', attrs=['blink'])
        print("")
        print("*** Welcome to ", end="")
        print(colored(welcome), end="")
        print("! ***")
        print("")

        return sftp

    except pysftp.AuthenticationException:
        print("Username " + SFTP_USER + " could not be authenticated. Exiting.")
        sys.exit()

    except pysftp.SSHException:
        print("Host: " + SFTP_NET + " could not be validated. Exiting.")
        sys.exit()

    else:
        print("Connection to host unsuccessful. Exiting")
