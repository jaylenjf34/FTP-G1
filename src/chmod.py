import pysftp

def chmod(conn, arg):

  if length(arg) < 2:
    print("must include file name and permission mask in octal: ex. 644")
    return

  local_file = arg[0]
  perms = arg[1]

  try:
    conn.chmod(local_file, perms)

  except:
    print("Error changing mode (permissions) on "+ local_file + ".")
