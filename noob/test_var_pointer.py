a = 1
print(id(a))
b = a
print(id(b))
b = 2
print(id(b))

b = b+1
print(id(b))

l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l))
