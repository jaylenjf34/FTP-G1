import pysftp
import getpass

def main():
    SFPT_URL = 'linux.cs.pdx.edu'
    SFPT_USER = input('Please enter your username: ')
    SFPT_PSWD = getpass.getpass()
    sftp = pysftp.Connection(SFPT_URL, username=SFPT_USER, password=SFPT_PSWD)
    print('Attepting connection to ' + SFPT_URL + '...')
    dir = sftp.pwd
    print(dir)
    sftp.close

if __name__ == "__main__":
    main()