demo=[12,323,42,441,"dsjnv","djs"]
c=[12,323,4,43,43,3]
d=("dad","aded","wda","qwdd","daw")        #tuple
demo.append(50)
print(demo)
demo.reverse()
print(demo)
print(demo.count(441))
demo.insert(3,100)
demo.remove(100)
del demo[3]
print(demo[:3])
print(demo)
a=[demo,c,d]
print(a)
x=[]
x.append(demo)
x.append(c)
x.append(d)

print(x)



