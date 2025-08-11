# what is a lambda function
# small, anonymous function - useful for concise operations
# used in functional programming, sorting, data transformations
# Syntax lamba arguments: expression

# conventional user defined function

# function to add two numbers together and return the result
def add_two_numbers(num1, num2):
    return num1+num2
print(add_two_numbers(1,2))

# adding two numbers - using a lambda function
add = lambda num1, num2:num1 + num2
print(add(2,3))

# Write a user defined function that iwll receive an integer parameter 
# the function will return the square of this number

def square(x):
    return(x**2)
print(square(10))
print(square(50))

numbers = [1, 2, 3, 4, 5]
print(square(numbers[0]))
print(square(numbers[1]))
print(square(numbers[2]))
print(square(numbers[3]))
print(square(numbers[4]))

# Write a user defined function that iwll receive an integer parameter 
# the function will return the square of this number
# write it via LAMBDA function

# or lambda x:x*x
squared_lambda= lambda x:x**2 
print(squared_lambda(51))

# common use cases
# 1: using lambda with map()
numbers= [1, 2, 3, 4]

numbers_map=list(map(lambda x:x**2, numbers))
print(numbers_map)
print(list(map(lambda x:x**2, numbers)))

# using lambda with filter()
number= [1, 2, 3, 4, 5, 6, 7]

# extract all of the even numbers and store them in a new list
new_even_list= list(filter(lambda x: x%2 ==0, number))
print(new_even_list)

print(list(filter(lambda x: x%2 ==0, number)))

# using lambda with sorted
fruits = ['apple', 'fig', 'strawberry', 'banana', 'cherry', 'avocado', 'tangerine']

# by default sorted sorts the list by alphabetical order
print(sorted(fruits))
# sort this list based off the charchets in each word
# this sorts it based of the length of each word
sorted_words= sorted(fruits, key = lambda word:len(word))
print(sorted_words)
# lambda word:len(word)

# convert each celsius reading to fahrenheit
# formula is: F = (C*9/5) + 32

celsius= [0, 100, 10, 20, 30, 40, 50]
# now we want to map it to the celsius list then convert it back into a list
fahrenheit = list(map(lambda C: (C*(9/5)) + 32, celsius))
print(fahrenheit)
print(list(map(lambda C: (C*(9/5)) + 32, celsius)))