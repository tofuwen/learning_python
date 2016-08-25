square = list(map(lambda x: x**2, range(10)))
print(square)

square = [x**2 for x in range(10)]
print(square)
print(type(square))

#set
s = {x**2 for x in range(4)}
print(type(s))

#dict
d = {'a' + str(x): x**2 for x in range(4)}
print(d)
print(type(d))

print(d.items())

for i, v in d.items():
    print(i)
    print(v)
