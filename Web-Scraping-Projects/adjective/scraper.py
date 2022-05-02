from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re

req = Request('https://www.talkenglish.com/vocabulary/top-500-adjectives.aspx', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

adj= []
   
#Quotes Section
products = soup.select('td>a')
for elems in products:
    adj.append(elems.text.strip())


with open('your_file.txt', 'w') as f:
    for item in adj:
        f.write("%s\n" % item)
        print(item)