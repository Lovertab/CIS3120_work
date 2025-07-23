# Import Libaries 

import requests 
from bs4 import BeautifulSoup

import pandas as pd

# Set the URL

url=


# Set headers!
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