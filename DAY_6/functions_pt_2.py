# zip()
# combines multiple lists into tuples
# if the lists have different lengths, zip() stops at the shortest


list1=[1, 2, 3]
list2=['a', 'b', 'c']

# generate pairs from list1 and list2
#eg: [(1, 'a'), (2, 'b'), (3, 'c')]

zipped_result=zip(list1,list2)
list(zipped_result)

#using a for loop with zip
# check this
# for var1, var2 in list(zipped_result):
#     print(var1, var2)
    
for var1, var2 in zip(list1, list2):
    print(var1, var2)

# uneve list what happens
list3=[1,2,3]
list4=['a', 'b', 'c', 'd']

print(list(zip(list3, list4)))


names=['alice', 'bob', 'charlie']
scores = [100, 80, 90]
# print(list(zip(names, scores)))

for name, score in zip(names, scores):
    print(f'{name} scored {score} points.')
    #  print(name, 'scored', score, 'points.')

zipped_data = list(zip(names, scores))
print(zipped_data)

# to undo this zip we use UNZIPPING
x, y = zip(*zipped_data)
print(x)
print(y)
print(list(x))
print(list(y))


# Using zip() with Dictionaries
keys = ['name', 'age', 'city']
values=['Alice', 25, 'New York']

person_info= dict(zip(keys, values))
print(person_info)
print(person_info['age'])
print(person_info['name'])
print(person_info['city'])

# list in tuples
# keys = ['name', 'age', 'city', 'skills']
# values=['Alice', 25, 'New York', [('coding'), ()'math)', ('language')]]



# applies a function to each element in a iterable
# LEARN FOR MIDTERM
# write a function that will receive one parameter and return its square
#one parameter means x 
def squared(x):
    return x**2
    
# find 12*2
# call the function
print(squared(12))

numbers=[1, 2, 3, 4, 5]
# num = float(input('enter a number'))
# print(f '')

for number in numbers:
    # to get the squared number of this list
    print(squared(number))



# via the map functions 
# map the squared funtion to each item in the numbers list
# when you use map to see it we need to say list
squared_numbers = list(map(squared, numbers))
print(squared_numbers)

word='fun'
print(word.capitalize())

words=['python', 'is', 'fun']
# capitalize each word
def capitalize_word(word):
    return word.capitalize()

capitalized_words= list(map(capitalize_word,words))
print(capitalized_words)

text= '         hello      '
print(text.strip())

messages = ['   hello    ', '    python', 'world      ']

# we say text because its expects a word not a list
def strip_blank_space(text):
    return text.strip()

# print(list(map(strip_blank_space, messages)))
# or
clean_messages =list(map(strip_blank_space, messages))
print(clean_messages)

# get it on one line with no brackets
for x in clean_messages:
    print(x, end = ' ')
    
# .filter()
# removes elements that do not satisy a condition
# create a function that will recieve an integer parameter. the function will return true if the interger is even and false otherwise. 

def is_even(num):
    if num%2==0 :
        return True
    else:
        return False
    
print(is_even(5))

# another way to write this
def is_even(num):
    return num% 2 == 0

print(is_even(10))

numbers = [10, 15, 22, 33, 40]

#apply a filter to the numbers via the is_even() functions
# using filter does the is_even function 
even_numbers= list(filter(is_even, numbers))
print(even_numbers)

words = ['Python', 'is', 'great', 'fun']
# find the wordsmore that 4 characters

def more_than_four_letters(word):
    if len(word)> 4:
        return True
    else:
        return False
print(more_than_four_letters('Baruch'))

# or can write like this
def more_than_four_letters(word):
    return len(word)>4
print(more_than_four_letters('pre'))

long_words= list(filter(more_than_four_letters, words))
print(long_words)

students = [
   {'name': 'Alice', 'score': 85},{'name': 'Bob', 'score': 45},
   {'name': 'Charlie', 'score': 78},{'name': 'Brandy', 'score': 55}
]

#use a filter to find all students who passed
# a passing grade is a score >= 80

print(students[1].get('score'))
print(students[2]['score'])


def has_passed(student):
    return student['score']>=80

students_passed =list(filter(has_passed, students))
print(students_passed)