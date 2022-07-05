from sys import argv

try:
  if argv[1]:
    pass
except IndexError:
  print("no args")