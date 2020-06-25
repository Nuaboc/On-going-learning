# Chapter 8
# Reading and Writing Files

import os
import shelve

# This create a folder in the mentioned directory
# os.makedirs('D:\\delicious\\walnut\\waffles')

# os.chdir('D:\\Pictures')

# os.path.getsize('D:\\Pictures')
# Don't know why these lines are not working.
# os.path.getsize('D:\\Programs Files HDD')


shelfFile = shelve.open('mydata')
cats = ['Pepe', 'Pooka', 'Pikachu']
shelfFile['cats'] = cats
shelfFile.close()
