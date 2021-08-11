
def save_connect(arg1) :
    connect_info=open('connect_info.txt', 'w')
    connect_info.write(arg1)
    connect_info.close()
