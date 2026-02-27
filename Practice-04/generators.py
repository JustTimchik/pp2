def square_generator(n):
    for i in range(n + 1):
        yield i * i   #same as return but does not exit the function, it allows the function to be resumed later on; also it is an iterator, so we need to use a loop to get the values one by one

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
a = int(input())
b = int(input())
for x in square_generator(n):
    print(x,end=' ')
print()
for y in even_numbers(n):
    print(y, end=',')
print()
for z in divisible_by_3_and_4(n):
    print(z, end=' ')
print()
for w in squares(a, b):
    print(w, end=' ')
print()
for v in countdown(n):
    print(v, end=' ')

#the loop is used to get our values one by one from the generator, as the generator is an iterator, we cannot get all the values at once, we need to use a loop to get them one by one