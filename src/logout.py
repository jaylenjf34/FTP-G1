import pysftp
import os
import datetime


def logout(conn):
    log = open(os.path.expanduser('logfile.txt'), 'a')
    log.write('Connection closed at: ' +
              datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S\n"))
    log.write('********************************************\n\n')
    log.close()
    conn.close()
    print("Connection to host closed. Returning control!")
    print("")
    os.sys.exit()
