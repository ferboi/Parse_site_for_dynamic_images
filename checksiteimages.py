"""This python script opens a site opens all images used by the site that have a url. 
If no image is opened it means the site stores all its images on the same machine used to host it."""

import urllib.request as urllib2
from bs4 import BeautifulSoup as bs4
import os
import re

def findImages(url):
    print('[*]Searching for Images on: ' + url)
    urlcontent = urllib2.urlopen(url).read()
    soup = bs4(urlcontent, features="html.parser")
    imgtags = soup.find_all('img')
    return imgtags

url = 'https://facebook.com'
testimagereturn = findImages(url)
print(testimagereturn)

imagelist = []

for image in testimagereturn:
    image = str(image)
    imagelist.append(image)

print()
print(imagelist)

#r'maplat=.*\&'

for image in imagelist:
    nextform = image.split('"')
    #finalform = re.findall(r'https:.*" ', image)
    for image2 in nextform:
        if 'https:' in image2:
            finalform = image2
            print('Opening: ' + finalform)
            os.system('firefox ' + finalform)
