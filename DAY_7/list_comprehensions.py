# find the sum of all odd and even numbers between 1 and 10 (inclusive)

# acculumators to store the odd/even sums
odd_sum=0
even_sum=0
for i in range(1,11):
    print(sum)
    if 1%2 == 0:
        print(f'{i} is even')
        even_sum +=i
    else:
        print(f'{i} is odd')
        odd_sum += i
print('\n\n')
print(f'the odd sum is {odd_sum}')
print(f'the even sum is {even_sum}')

# pring all the integers from 1 to 10(inclusive) using a while loop


x=1
while x<11:
    print(x)
    x +=1
    
 # find the sum of all odd and even numbers between 1 and 10 (inclusive) using a WHILE loop

even_sum=0
odd_sum=0
i=1
while i<11:
    if 1%2 == 0:
        print(f'{i} is even')
        even_sum +=i
    else:
        print(f'{i} is odd')
        odd_sum += i
    i +=1
print('\n\n')
print(f'the odd sum is {odd_sum}')
print(f'the even sum is {even_sum}')

# generate the integers from 1 to 10 (inclusive) and put them in a list 

numbers=[]
for i in range(1,11):
    print(1)
    numbers.append(i)
print(numbers)

# NEW TOPIC
# Using a list comprehension
# i reprsents each integer form 1-10
# the first 1 reprsents the i from the numbers.append(i)
numbers = [ i for i in range(1,11) ]
print(numbers)

# list comprehension - loops and if statements

# even numbers between 1 to 10 inclusive
even_nums=[ i for i in range(1,11) if i%2 ==0]
print(even_nums)


# find the sum of all numbers in the even_numbers list
# use sum function
sum(even_nums)

# odd numbers between 1 to 10 inclusive
odd_nums=[ i for i in range(1,11) if i%2 ==1]
print(odd_nums)

# find the average of all odd numbers between 1 and 10 (inclusive)
average= sum(odd_nums)/len(odd_nums)
print(average)

# find words with more that 4 characters
words= ['apple', 'is', 'a', 'fruit', 'tree', 'red']

# without using a list comprehension

for word in words:
    if len(word)> 4:
        print(word)
        
        
#with a list comprehension
# find words with more that 4 characters
words= ['apple', 'is', 'a', 'fruit', 'tree', 'red']
long_words=[word for word in words if len(word)>4]
print(long_words)

# Reverse each word in a sentence
sentence = 'Python is amazing'
# extract the first word in the sentence
sentence.split()[0]
# Output: 'nohtyP si gnizama'
sentence.split()[0][::-1]
sentence.split()[1][::-1]
sentence.split()[2][::-1]
# without using a list comprehension
sentence.split()

reversed_words = []
for word in sentence.split():
    # print(word[::-1])
    reversed_words.append(word[::-1])
print(reversed_words)

print(' '.join(reversed_words))
reversed_word= ' +'.join(reversed_words)
print(reversed_word)
# ' ,'.join(reversed_words)

sentence = 'P#yt#honi#s#amazin#g'
sentence.split('#')

fruit='orange'
fruit[::-1]


# reversed each word in the sentence via a list comprehension
sentence='Python is amazing'
sentence.split()

reversed_words_list = '== '.join([word[::-1] for word in sentence.split()])
print(reversed_words_list)

# without a list comprehension
matrix = [[1,2],[3,4], [5,6]]
# flatten the above into a single list
# output: [1,2,3,4,5,6]
flattended=[]
for row in matrix:
    # print(row)
    for num in row:
        # print(num, end=' ')
        flattended.append(num)
    print(flattended)

# with a list comprehension
matrix = [[1,2],[3,4], [5,6]]
flattended=[num for row in matrix  for num in row]
print(flattended)

#find all the vowels that exist in the sentence above
sentence_vowel= 'the lazy dog jumped over the brown fox'
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence_vowel:
    if char in vowels:
        print(char)
        

sentence_vowel_list= 'the lazy dog jumped over the brown fox'
vowel_list=[char for char in sentence_vowel_list if char in vowels]
print(vowel_list)

# another way
x= [char for char in sentence_vowel_list if char =='a' or char =='e' or char=='i' or char== 'o' or char =='u']
print(x)

