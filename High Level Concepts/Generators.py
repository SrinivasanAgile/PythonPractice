
#generator function to print squares upto 10

user_input=int(input("Enter the number upto which squares has to be calculated:"))

def func(n):
    i=1
    while i<=user_input:      # Map the user input into while condition
        a= i*i                # introduce a new variable to perform squaring operation and yield that value
        yield a
        i += 1                  # increment the index for subsequent process


values = func(user_input)
print(values)

print(next(values))             # manual value of printing 1st item in the list
print("Hi")                     # can be used to replace with logic to be executed based on first item in the list
print(next(values))             # printing of subsequent values

#for i in values:               # Loop to iterate throughout the generator function
#   print(i)

#Generator function to print fibbonacci numbers

user_value=int(input("Enter the number upto which fibbonaci numbers has to be calculated:"))

def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s

for x in fib():
        if(x>user_value):
            break
        print(x)