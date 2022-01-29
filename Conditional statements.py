print("check")

print("This program is to compare 2 numbers and will identify the greatest number amongst it")
print("Enter 1st number: ")
a=int(input())
print("Enter 2nd number: ")
b=int(input())

if a>b:
    print(a, " is greatest")
else:
    print(b, "is greatest")


print("This program is to compare 3 numbers and will identify the greatest number amongst it")
print("Enter 1st number: ")
a=int(input())
print("Enter 2nd number: ")
b=int(input())
print("Enter 3rd number: ")
c=int(input())

if ((a>b) and (a>c)):
    print(a, " is greatest")
elif b>c:
    print(b, "is greatest")
else:
    print(c, "is greatest")

print("this program is to compare entered numbers with a pre-defined value")
print("Enter your number:")
a=int(input())
if(a==10):
    print("case valid")
else:
    print("Not valid")