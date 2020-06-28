# Doing Math With Python
# Chapter 1 Working With Numbers

n = 25.5 * 2.54 / 100

print(n)

print(round(n, 4))

f = 98.6

c = 37

fahrenheit = c * 9/5 + 32

celsius = f - 32 * 5/9

print(fahrenheit)
print(celsius)
print("........................................................................................................")

for i in range(20):
    if i % 2 == 0:
        print(1 + i)
