# Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set URL
url ='https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster'

# Set the headers 
# headers Source: https://www.zenrows.com/blog/web-scraping-headers#user-agent
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive'
  }
# importing raw html into beautiful soup
soup= BeautifulSoup(page.content, 'html.parser')

td_tags=soup.find_all('td', class_='height')

heights=[]
for td_tag in td_tags:
    # print(td_tag.get_tet())
    # raw_height =td_tag.get_tet()
    # print(raw_height)
    # feet=float(raw_height[0])
    # # we need the 2: because it was cutting off the 11 to 1 this makes it back 11
    # inches=float(raw_height[2:])
    # print(f'raw height: {raw_height}, feet: {feet}, inches: {inches}')
    # height.append(td_tag.get_tet())
    

    
    heights=[]
for td_tag in td_tags:
#    raw_height =td_tag.get_tet().split('-')
   raw_height =td_tag.get_tet()
   split_height=raw_height.split('-')
   feet=float(raw_height[0])
   inches=float(raw_height[1])
   height_in_inches= feet* 12+inches
#    print(f'raw height: {raw_height}, after using split: {split_height}')
#    print(f'raw height: {raw_height}, feet: {feet}, inches: {inches}')
#    print(f'raw height: {raw_height}, height_in_inches: {height_in_inches}')
heights.append(height_in_inches)
avg_height= sum(heights)/len(heights)
print(f'the avg height is {round(avg_height,2)} inches')

   