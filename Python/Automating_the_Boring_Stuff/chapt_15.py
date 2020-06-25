# Chapter 15
# Keeping Time, Scheduling Tasks, and Launching Programs

import time


"""def calcProd():
   # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))"""

for i in range(5):
    print('tick')
    time.sleep(1)
    print('tock')
    time.sleep(1)

