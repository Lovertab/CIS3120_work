# 1. Write a function that receives one parameter and returns its square


def square(x):
    return(x**2)
print(square(2))

# 2. Write code that sends a GET request to "https://books.toscrape.com" and stores the HTML response

import requests
# from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'

page=requests.get(url)
print(page.status_code)


# Write a function that takes a string and returns True if it's a palindrome (same forward and backward), else False

# [::-1]
def palindrome(x):
    return x== x[::-1]

words= ['dad', 'mom', 'sis', 'racecar', 'brown']
print(palindrome(words))

for word in words:
    if palindrome(word):
        print("True")
    else:
        print("False")
        
        
        
  