import os 

def lrename(args):
    if len(args) < 2:
        print("Error, must provide original and new filename Ex: lrename old/name new/name")
        return
    orig_name = args[0]
    new_name = args[1]
    os.system('mv ' + orig_name + ' ' + new_name)
