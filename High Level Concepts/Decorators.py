def div(a,b):
    return a/b

def swap_func(func1):
    def inner(a,b):             #function signature of this inner function should match with function in line 1
        if(a<b):
            a,b=b,a             # swapping is done to make sure that numerator is always greater than denominator
            return func1(a,b)   # returns the updated values(a,b) to the div(a,b) function
    return inner

division = swap_func(div)
                               # now, when division is called, it triggers the function which has another function into it,
print(division(2,4))            # which will first make-up or decorate the parameters and then pass it to relevant function.

def diff(a,b):
    return a-b

difference = swap_func(diff)
print(difference(10,12))

