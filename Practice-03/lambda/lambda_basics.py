x = lambda a, b : a * b  #creating a lambda function and assigning it to a variable x; the expression a * b is evaluated and returned when the function is called with two arguments a and b
a=int(input())
b=int(input())
print(x(a, b))  #calling the lambda function x with the arguments a and b

def function(n):
    return lambda a : a * n  #defining a function that returns a lambda function that takes a parameter a and multiplies it by n
doubler = function(2) #assigning the value of n to 2, creating a lambda function that doubles its input and assigning it to the variable doubler
tripler = function(3) #assigning the value of n to 3, creating a lambda function that triples its input and assigning it to the variable tripler
print(doubler(11)) #calling the lambda function doubler with the argument 11, which returns 22 (11 multiplied by 2)
print(tripler(11)) #calling the lambda function tripler with the argument 11, which returns 33 (11 multiplied by 3)

