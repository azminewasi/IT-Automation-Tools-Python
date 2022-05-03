from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re

req = Request('https://preply.com/en/blog/interjections/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

interjections= []
   
#Quotes Section
products = soup.select('tr>td>b')
for elems in products:
    interjections.append(elems.text.strip())


with open('interjections.txt', 'w') as f:
    for item in interjections:
        f.write("%s\n" % item)
        print(item)