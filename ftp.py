from ftplib import FTP
print('This is FTP')

def terminal() :
    line = input("$")
    while line != "logout":
    # some more inputs for the FTP server
        line = input("$")


terminal()
