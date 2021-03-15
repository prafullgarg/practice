tup=(23,41,4313)  # declared using round braces()
set={1,1,1,1,2,3,3}   # declared using curly braces {}
print(tup.count(41))
print(tup.index(41))
set.remove(1)
set.add(5)
print(set.difference(tup))
print(set.pop())
print(tup , set)

