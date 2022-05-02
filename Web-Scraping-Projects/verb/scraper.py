from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re

req = Request('https://7esl.com/list-of-nouns', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

nouns= []
   
#Quotes Section
products = soup.select('ul>li')
for elems in products:
    nouns.append(elems.text.strip())


with open('your_file.txt', 'w') as f:
    for item in nouns:
        f.write("%s\n" % item)
        print(item)