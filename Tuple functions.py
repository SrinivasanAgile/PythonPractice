#    0  1     2    3     4      5       6       7   8    9   10  # Positive Index
a = (1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33)
#                                                   -3  -2   -1
print(a)            # prints whole Tuple
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index;
print(a[3:-1])      # start index : end before index;
print(a[4:])        # start index : till end of Tuple;
print(a[:9])        # from start of Tuple: end before index
print(a[:])         # from start of Tuple: till end of Tuple
print(a[0:11:2])    # start index : end before index : jump
print(a[::3])       # from start of Tuple: till end of Tuple: jump
print(a[::-1])      # reversing a Tuple using jump as -1"""

a = (1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33)
print(a)
x = a[::-1] # Stores a newly created tuple in 'x' variable
print(x)
y=x[::-1]
print(y)

a = (1,22,3.4,True,'hello',3.4,1,1,1,1,1,1)
x = a.count(1)
print(x)


a = [1,22,3.4,True,'hello',3.4,1,1,1,1,1,1]
x = a.count(909)
print(x)