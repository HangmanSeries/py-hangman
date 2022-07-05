from requests import get, ConnectionError

try:
  foods = \
	  get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/food.txt").text.split()
    # ['burger','pie']
  music_instruments = \
	  get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/music_instruments.txt").text.split()
    # ['flute', 'clarinet']
  coding = \
  	get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/coding.txt").text.split()
    # ['scope', 'comment']
  fruits = \
  	get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/fruit.txt").text.split()
    # ['apple', 'banana']
except ConnectionError:
  print("It seems you're offline.")
  exit()
