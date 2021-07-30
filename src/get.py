import pysftp

def get(conn, arg):
  remote_file = conn.pwd +'/'+ arg[0] 

  try:
    conn.get(remote_file)
  except:
    print('Could not get')