from random import shuffle, randint
from os import system

# --- Formatting ---

c = {
	'reset': '\033[0m',
	'gray':  '\033[90m',
	'green': '\033[92m',
	'red':   '\033[91m',
}

def clear():
	system('clear')

def printList(words):
	final = ''
	for i, word in enumerate(words):
		if i > 0: 
			final += c['gray']
			final += ', '
		final += word

	return final + c['reset']

# --- Read File ---

file = open('u0.txt', 'r')
fileLines = list(file)
fileLineCount = len(fileLines)
shuffle(fileLines)
file.close()

# --- Make Translation List ---

translations = []

for line in fileLines:
	line = line.replace('\n', '')
	spanish, english = line.split(' == ')

	spanish = spanish.split(' / ')
	english = english.split(' / ')

	translations.append([spanish, english])

# --- Ask Questions ---

for i, translation in enumerate(translations):
	spanish, english = translation

	while True:
		clear()
		print(f'{c["gray"]}Question {i+1}/{fileLineCount}{c["reset"]}\n')
	
		terms = printList(english)
		print(terms)
		print('\n\n')

		answer = input(f'{c["gray"]}> {c["reset"]}')

		if answer != '': break

# --- Manage Answers ---

	print()

	if answer in spanish:
		print(f'{c["green"]}YOU GOT IT :D{c["reset"]}')
	else:
		s = 's' if len(spanish) > 1 else ''
		print(f'{c["red"]}WRONG >:({c["reset"]}')
		print(f'Answer{s}: {printList(spanish)}')

	input()

