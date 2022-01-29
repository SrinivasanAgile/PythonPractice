#    0123456789     # Positive Index
a = "helloworld"
#             -1    # Negative Index
print(a)            # prints whole string
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index (1-8)
print(a[3:-1])      # start index : end before index (3-8)
print(a[4:])        # start index : till end of string
print(a[:9])        # from start of string : end before index
print(a[:])         # from start of string : till end of string
print(a[0:10:2])    # start index : end before index : jump (0-9)
print(a[::3])       # from start of string : till end of string : jump
print(a[::-1])      # reversing a string using jump as -1


a = 'hello world'
print(a.isalpha())

a = "The quick brown fox jumps over the lazy dog idiom"
x = a.count('z')
print(x)

a = 'Green'
b = 'Black'
mystr = "Colours = {},{},Red"

x = mystr.format(a,b)
print(x)


