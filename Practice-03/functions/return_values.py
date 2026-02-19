def sum(a,b): #defining a function 
  return a+b #returning an integer value which is the sum of a and b

x=int(input())
y=int(input())
result=sum(x,y)  #calling the function and storing the returned value in a variable named
print(result)  #printing the result

c=5+sum(10,20)  #using the function in an expression, it will return the sum and then add 5 to it
print(c)  #printing the value of c


def factorial(n): #defining a function to calculate the factorial of a number
  if n==0:  #base case, if n is 0, return 1
    return 1
  else:  #recursive case, if n is greater than 0, return n multiplied by the factorial of n-1
    return n*factorial(n-1) #returning the value of n multiplied by the result of calling the factorial function with n-1 as the argument
  
print(factorial(5))  #calling the factorial function with 5 as the argument