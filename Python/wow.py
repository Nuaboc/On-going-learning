x = .01

y = x

l = []

for i in range(1, 31):
    y = x * 2
    x = y
    l.append(y)

for i in enumerate(l):
    print(i)
