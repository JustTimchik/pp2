nums = [1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x % 2 == 0, nums)) #using the filter function to apply a lambda function that filters out odd numbers from the list nums, and converting the result to a list
print(filtered)
