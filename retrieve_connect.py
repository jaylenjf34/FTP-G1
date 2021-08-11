import pysftp

def retrieve_connect():
    file1 = open('connect_info.txt', 'r+')
    host = file1.readline()
    return host
