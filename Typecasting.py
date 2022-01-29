print("This file is used for practising the learnt typecasting concepts")
"""
a=int(10)
print(a, type(a))

b=str(10.25)
print(b, type(b))

c="Srini"
print(c, type(c))

"""

print("Enter a value")
a=int((input()) #by default, input() has a string datatype, hence, to get integers, typecasting has to be done
print("Entered value is: ",a)

print("Enter another value to append: ")
b=int (input())
print("appended value is: ", a+b) # if variables are not typecasted, then error occurs while concatenation

