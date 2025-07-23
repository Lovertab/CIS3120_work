# Importing Libraries
import requests
from bs4 import BeautifulSoup

# Set the URL

url = "https://avinashjairam.github.io/syllabus.html"

# make a request to the server

page= requests.get(url)

# view the status code

print(page.status_code)

# we want to see the email with the id call email we need to tell the BOT to look for the paragraph tags only that has id email.

# peek at raw html

print(page.content)

# import raw html into beautifulsoup

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# locate the p tag that contains an id = email

email_tag = soup.find('p', id = 'email')
print(email_tag)

# extract the email form the tag

print(email_tag.text)
# OR
print(email_tag.get_text())

# ANOTHER WAY
email = email_tag.text
print(email)

email = email_tag.get_text()
print(email)


# USING FIND ALL 

email_tags = soup.find_all('p', id='email')
email_tags
email = email_tags[0].get_text()
print(email)