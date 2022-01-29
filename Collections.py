"""
This exercise is used to practice collections in Python, we shall look into
List
Tuple
Set
and default methods that has inside it
"""

print("works right - check")     #to check if starts correctly
"""
#List examples
a = [1,2,3,4,5]
b = [1.23,2.34,2.568,2.10]
c = ['a','c',"Srini", "Mani", "Vidya"]

e = [1, 2.34, 'a', "name", True, 3j]
#d = [a,b,c,e]

#print(d, type(d))
a[2]=1506 #item assignment in list possible

print(a)
a.append(2)
print(a)
a.pop(4)
print(a)
#a.count(2)
print(a.count(2))
a.insert(1,43)
print(a)
print(b)
b.clear()
print(b)
"""

#Tuple
"""
a = (1,2,2,3,1.23,'a', "test")

print(a, type(a))

print("number of time 3 is repeated is ", a.count(3))
print("number of time 2 is repeated is ", a.count(2))

print(a[5])

print(a)

# a[5]= 15  # Item assignment not supported in tuple, its methods are also very limited when compared to list

print(a[5])
"""

#Set

a={1,3,2,1.562}
print(a, type(a))
b={3,1.562, 1, 1,2,2,2}
print(b, type(b))
print(a.intersection(b))
print(a.difference(b))
print(a.difference_update(b))
print(a.issubset(b))
print(b.issuperset(a))




