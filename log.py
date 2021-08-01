import os


def log(action):
    log = open(os.path.expanduser('logfile.txt'), 'a')
    log.write(action + '\n')
    log.close()
