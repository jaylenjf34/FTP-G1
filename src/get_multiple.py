import pysftp
from src.get import get

def get_multiple(conn, args):

  try:
    for i in args:
     conn.get(conn.pwd +'/'+ i )
  except:
    print("could not get multiple")