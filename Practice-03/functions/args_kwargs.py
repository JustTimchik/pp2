def func_with_args(*whatever):  #defining a function that takes an unknown number of arguments
  print(whatever[0])  #printing the value of the first argument, which is at index 0

func_with_args(1, 2, 3, 4, 5)  #calling the function with multiple arguments

tuple_of_args=(10, 20, 30)  #creating a tuple of arguments
func_with_args(*tuple_of_args)  #calling the function with the tuple of arguments

def func_with_kwargs(**whatever):  #defining a function that takes an unknown number of keyword arguments
  print(whatever["name"])  #printing the value of the keyword argument with the key "name"

func_with_kwargs(name="Alice", age=30)  #calling the function with keyword arguments

dict_of_kwargs={"name": "Bob", "age": 25}  #creating a dictionary of keyword arguments
func_with_kwargs(**dict_of_kwargs)  #calling the function with the dictionary of keyword arguments