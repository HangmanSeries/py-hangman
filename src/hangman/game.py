from colorama import Fore, Style, init
from .utils import WordGenerator, ConfigLoader
from .scoring import *
from string import ascii_letters
from platform import system
# from .prompts import 

if system() == 'Windows':
  init()

async def generate():
  global string_category, word
  # choosing a word
  wgen = WordGenerator()
  category = wgen.generate_category()
  string_category = category.to_string()
  word = wgen.generate_word(category)

async def load_config():
  global config
  # config file
  config = ConfigLoader()
  config.ensure_config()

async def main(user):
  await generate()
  await load_config()
  print(f"Welcome {user}")
  # points
  points = 0

  # returns a set (just like list but no duplicates (easy hack))
  def indices(word, letter):
    indices = set()
    for x in range(len(word)):
      if word.find(letter, x) != -1:
        indices.add(word.find(letter, x))
    return indices

  # all alternative but False if ' '
  def all_not_blank(iterable):
    for element in iterable:
      if element == ' ':
        return False
    return True

  # any alternative but False if all are ' '
  def any_wrong_letter(iterable):
    for element in iterable:
      if element != ' ':
        return True
    return False

  # ensure lives
  def lives_color(lives):
    r = Fore.RESET
    if lives == 3 or lives == 2:
      return Fore.YELLOW + str(lives) + r
    elif 10 >= lives >= 4:
      return Fore.GREEN + str(lives) + r
    else:
      return Fore.RED + str(lives) + r

  # lives
  lives = config.get_setting('lives')
  # print(lives)

  # welcome message
  print("Welcome to the Game of Hangman :D\n")

  # guessed letters
  guessed_letters = [' ' for _ in range(len(word))]
  wrong_letters = [' ' for _ in range(lives)]

  while True:
    # letters guessed
    print(Fore.GREEN + Style.BRIGHT + "|  W O R D  |" + Style.RESET_ALL)
    # Category
    print("Category: {}".format(string_category))
    for x in guessed_letters:
      print(x, end=" ")

    # new line
    print()
    # blanks
    for x in range(len(word)):
      print("\u203e", end=" ")

    if any_wrong_letter(wrong_letters):
      print((Fore.RED + "\tWrong letters: " + Fore.RESET).expandtabs(6))
      for x in wrong_letters:
        print(x, end=" ")

    # if all blanks are filled up
    if all_not_blank(guessed_letters):
      print(f'\nAnswer: {word}')
      print(f"Lives left: {lives}")
      print("complete!")
      exit()

    if not lives:
      print("You lose!")
      print("Answer: {}".format(word))
      break

    # number of lives
    print(f"\nLives: {lives_color(lives)}")

    # simply input
    letter_input = input("\n=> ")

    # exit
    if letter_input == 'exit':
      break
    # player giving up
    elif letter_input == "giveup":
      if lives == 3:
        print("Answer:", word)
        break
      else:
        print("You cannot give up until you have 3 lives left.")
    # not 1 letter
    elif len(letter_input) != 1:
      print("letter please.")
    # empty string
    elif letter_input == '':
      print("Letter letter LEEEEETTTTTEEERRRRRR!")
    elif letter_input not in ascii_letters:
      print("Not a symbol")
    elif letter_input == 'clue':
      print("Starts with {}".format(word[0]))
    # letter not in chosen word
    elif letter_input not in word:
      print("wrong letter :P")
      print("-100 points :P")
      points = wrong_answer(points)
      if letter_input not in wrong_letters:
        lives -= 1
        wrong_letters.append(letter_input)

    # correct letter
    elif letter_input in word:
      # if letter not in guessed letters
      if letter_input not in guessed_letters:
        print("letter guessed!")
        print("+100 points :)")
        points = correct_answer(points)
        guessed_letters[word.index(letter_input)] = letter_input

        # if a letter has more than two characters on a word
        if word.count(letter_input) >= 2:
          for x in indices(word, letter_input):
            guessed_letters[x] = letter_input
      # if letter already guessed
      else:
        print("letter already guessed.")
