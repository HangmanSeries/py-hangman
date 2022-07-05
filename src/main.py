from asyncio import run

print("Hangman v1.0")

from hangman.utils import no_argv_indexerror
from hangman.prompts import login, create_account

argvval = no_argv_indexerror(1)

if not argvval:
  user_login = login()
  if not user_login:
    create_account()

  print("Loading game...")

  from hangman.game import main

  if __name__ == '__main__':
    run(main())
else:
  print("arg: {}".format(argvval))
