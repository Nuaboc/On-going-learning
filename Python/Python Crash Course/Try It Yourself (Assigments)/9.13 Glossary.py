# 9.13

from collections import OrderedDict

glossary = OrderedDict()

glossary = {
    'method': '\nMethods in Python are like build-in functions.',
	'string': '\nA string is a series of characters.',
	'.append': '\nThe ".append()" method adds a new element to a list.',
	'tuple': '\nPython call "immutable" values that cannot change, such as a tuple.',
	'dictionaries': '\nDictionaries are collections of key-value pairs. ' +
	'Every key is connected to a pair.'
	}

for words in glossary.values():
    print(words)

print ('\nadding terms..........................................................')

glossary['del'] = '\n"del" is a build-in funtion on Python to delete specific data in a list, or in a dictionary.'

glossary['variable'] = '\nA variable is a piece of data that holds a value.'

glossary['if statements'] = '\nAn "if-statement" is an expression that can be evaluated as "True" or "False" and is' \
                            'called a conditional test. '

glossary['boolean'] = '\nA boolean expression is another name for a conditional test.'

glossary['import this'] = '\n"import" is the way Python brings other scripts for the program you are working on.'

for meaning in glossary.values():
	print (meaning)