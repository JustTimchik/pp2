def func_with_arguments(name):  #defining a function with an argument named name
  print("Hello " + name)  #printing the value of name

def func_with_arguments2(x, y=5): #defining a function with two arguments, y has a default value of 5
  print(x+y)

def func_with_arguments3(x, y): #defining a function with two arguments, both are required
  print(x*y)

name=input()
a=int(input())
b=int(input())
func_with_arguments(name)  #calling the function with an argument
func_with_arguments2(a)  #calling the function with one argument, b will take the default value
func_with_arguments3(a, b)  #calling the function with two arguments