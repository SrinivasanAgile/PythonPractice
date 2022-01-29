#    0  1     2    3     4      5       6       7   8    9   10  # Positive Index
a = [1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33]
#                                                   -3  -2   -1
print(a)            # prints whole List
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index;
print(a[3:-1])      # start index : end before index;
print(a[4:])        # start index : till end of List;
print(a[:9])        # from start of List: end before index
print(a[:])         # from start of List: till end of List
print(a[0:11:2])    # start index : end before index : jump
print(a[::3])       # from start of List: till end of List: jump
print(a[::-1])      # reversing a List using jump as -1


print([1,2,3] + [33,44,55])
print([1,2,3] * 3)

a = [1,22,3.4,True,'hello',3.4]
a.append(100)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.pop()
print(a)


a = [1,22,3.4,True,'hello',3.4]
a.pop(0)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.insert(0,122)     #(position,value)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.remove(22)
print(a)


a = [1,22,3.4,True,'hello',3.4]
a.clear()   #(position,value)
print(a)


a = [1,22,3.4,True,'hello',3.4]
x = a.index('hello')
print(x)


a = [1,22,3.4,True,'hello',3.4]
x = a.count(0)
print(x)

a = [1,22,3.43,1,1,1,1,1,1]
a.sort()
print(a)
a.reverse()
print(a)

a = [1,22,3.43,1,81,17,14,1,21]
b = [111,222,333]
a.extend(b)
print(a)
print(b)

a = [1,22,3.43,1,81,17,14,1,21]
b = (111,222, 333)   # Its a tuple
a.extend(b)         # extend can be used to concatenate list and tuple, addition of 2 different data types throws an error)
print(a)
print(b)

