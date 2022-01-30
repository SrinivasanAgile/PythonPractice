a=[2,5,12,13,15]

ab=iter(a)  #assign a variable as an iterator

print(a[2])
print(next(ab))
print(ab.__next__())

for i in a:
    print(i)