# Import Libaries

import requests
from bs4 import BeautifulSoup
# os to create files on your machines to determine path on machine
import os 
# bytesio to download
from io import BytesIO
# render images
import matplotlib.pyplot as plt
from PIL import Image

# Set the URL
url = 'https://bronxzoo.com/animals/our-animals'

# Make a request to the server
page=requests.get(url)

# scrape only if request is successful

if page.status_code == 200:
    #import the raw html into BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all of the name tags with the class 'type-caption'
    name_tags= soup.find_all('p', class_='type-caption')
    
    # extract the names
    for name_tag in name_tags:
         # .strip removes extra spacing at the beinnging and after the word
        print(name_tag.get_text().strip())
       
    # find all of the image tags with the class 'image-fluid'
    image_tags= soup.find_all('img', class_='image-fluid')
    # print(image_tags)
    
    # get the source url for all images
    # for image_tag in image_tags:
    #     # the ['src] gives us the soruce attribute url.
    #     print(image_tag['src'])
        
    # Pair the names with the image url
    for name_tag, image_tag in zip (name_tags, image_tags):
        animal_name= name_tag.get_text().strip()
        image_url= image_tag['src']
        print(animal_name,image_url)
        
        # download the image
        image_response= requests.get(image_url)
        # image.open creates the pictures image response. content think of it like page.content
        img= Image.open(BytesIO(image_response.content))
        
        # Display the image using plt
        # plt.imshow(img)
        # plt.axis('off')
        # plt.title(animal_name)
        # plt.show()
        
        # print(image_url)
        
        # extract the filename form the image url
        # so when we download the file we have the actuall correct name
        filename = os.path.basename(image_url)
        # so when we download the file we have the actuall correct name
        # print(filename)
        
        # make a request to the server to download the image
        with request.get(image_url, stream = True) as image_response:
            # open a file with the same name as the image
            with open(filename, 'wb') as file:
                # for each chunck of data recieved, we are writing  it to the file
                for chunk in image_response.iter_content(chunk_size=8192)
                file.write(chunk)
                
                # print a message indicating that a file has been downloaded
                print(f'Downloaded: {filename}')
        
        
        
        
        
        
        
        
        
#-------------------------------------------------
        # EXAMPLE OF ZIP  
    # names = ['bob', 'mike', 'alice', 'lisa', 'rob']
    # scores = [90, 85, 94, 87, 75]
    
    # for name, score in zip(names, scores):
    #     print(name, score)