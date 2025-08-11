# Importing Libraries
import requests
from bs4 import BeautifulSoup

import pandas as pd
# Set the URL

url = "https://zicklin.baruch.cuny.edu/Department/cis-faculty/"

# Set the headers and make a request to the server
# ----------------------------------------------
# headers Source: https://www.zenrows.com/blog/web-scraping-headers#user-agent

# x = {
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#   'Accept-Language': 'en-US,en;q=0.9',
#   'Connection': 'keep-alive'
#   }



# # make a request to the server

# page= requests.get(url, headers=x, verify = False)
# --------------------------------------------
# WAY TO WRITE IT OR THE ONE ON TOP!!!
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive'
  }



# make a request to the server

page= requests.get(url, headers=headers, verify = False)
# view the status code

print(page.status_code)

# we want to see the email with the id call email we need to tell the BOT to look for the paragraph tags only that has id email.

# peek at raw html
# print(page.content)
# import raw html into beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# FIND ALL a tags with class = 'email'
# need the _ in the class that's how we need to write it
email_tags= soup.find_all('a', class_='email')

# print('total emails found:', len(email_tags))

# create an empty list to store emails
emails=[]
for email_tag in email_tags:
    # print(email_tag.get_text())
  emails.append(email_tag.get_text())
# print(emails)
    
# SCRAPING for the faculty names
name_tags= soup.find_all('h2', class_='facultyName')
# how much names in total
# print('total names found:', len(name_tags))

names=[]
for name_tag in name_tags:
    # print(name_tag.text)
    names.append(name_tag.get_text())
# print(names)
    
    
    # buliding a pandas dataframe
    
email_data= {
        # key: value pairs
        # i want 
        # 'name': names,
        # email: emails
        'Name': names,
        'Email': emails
    }
    
email_df= pd.DataFrame(email_data)
print(email_df)
    # print(len(names))
    # print(len(emails))
    
    # export dataframe as a csv file, csv: common sepearted values 
email_df.to_csv('Faculty_Email.csv', index = False)
    
    
    
    # -----------------------------------------
    
    #fruits and animals example
    # fruits = ['apples', 'lemon']
    # fruits.append('watermelon')
    # fruits.append('blueberries')
    
    # fruits = fruits+['pineapple','oranges','banna']
    # print(fruits)
    
    # animals=[]
    # animals.append('dog')
    # animals.append('cats')
    # print(animals)