# Import Libary

import requests

# SET the URL

url = 'https://en.wikipedia.org/wiki/Pet'

# Make a request to the server

page = requests.get(url)

# Check the status code

page.status_code

# words= page.text
# pets = ["cat", "dog", "snake", "fish", "bird", "monkey", "iguana"]
# pets1 = ["cats", "dogs", "snakes", "fishs", "birds", "monkeys", "iguanas"]

# for pet in pets:
#     print(f'{pet} (number of mentions): {words.count(pet)}')

# for pet1 in pets1:
#     print(f'{pet1} (number of mentions): {words.count(pet1)}')
    
sentence = 'the brown fox jumped over the lazy dog'
# how much times does the word "the" show up
print(sentence.count('the'))