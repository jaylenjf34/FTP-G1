import pysftp
import getpass
import sys
from termcolor import colored


def login():
    SFTP_NET = input('Please enter the hostname: ')
    SFTP_USER = input('Please enter your username: ')
    SFTP_PSWD = getpass.getpass()

    SFTP_NET = 'linux.cs.pdx.edu'
    SFTP_USER = 'keca2'
    #SFTP_PSWD = ''

    print("")
    print('Attempting connection to ' + colored(SFTP_NET, 'blue') +
          ' with user ' + colored(SFTP_USER, 'green') + '...')
    print("")

    try:
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
