from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re
import time

req = Request('https://play.google.com/store/apps/collection/cluster?clp=igM4ChkKEzQ4MjY4Mjc3ODc5NDY5NjQ5NjkQCBgDEhkKEzQ4MjY4Mjc3ODc5NDY5NjQ5NjkQCBgDGAA%3D:S:ANO1ljJXggI&gsr=CjuKAzgKGQoTNDgyNjgyNzc4Nzk0Njk2NDk2ORAIGAMSGQoTNDgyNjgyNzc4Nzk0Njk2NDk2ORAIGAMYAA%3D%3D:S:ANO1ljJscA0', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')


links = [a for a in soup.select('.b8cIId ReQCgd Q9MA7b')]



adj= []


products = soup.select('a')
for elems in products:
    adj.append(elems['href'])

final=[]

for i in adj:
    s=i.split("=")
    try:
        if "com.gameloft.android" in s[1]:
            final.append(s[1])
    except:
        continue


fd=[]
for f in final:
    if f not in fd:
        fd.append(f)
print(len(fd))


databank={}

from google_play_scraper import app

for game in fd:
    result = app(
        game,
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
        )
    databank[game]=result
    time.sleep(1)
    print(game,"done")


print ("\n\n\n")
df = pd.DataFrame(databank)
print (df)

df.to_excel("Data.xlsx")
df.to_csv("data.csv")



"""  

with open('your_file.txt', 'w') as f:
    for item in adj:
        f.write("%s\n" % item)
        print(item)
"""