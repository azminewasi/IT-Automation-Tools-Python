from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re

req = Request('https://fourminutebooks.com/best-happiness-books/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

book= []
quotes=[]
the_book_in_one_sentence=[]
why_should_you_read_it=[]
takeways=[]
takeway_1=[]
takeway_2=[]
takeway_3=[]



#Book name Section
for link in soup.findAll('a'):
    a=link.get('href')
    if a!=None:
        if len(a)>=2:
            if a[0]=="#" and a[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                book.append(a)

    
#Quotes Section
products = soup.select('blockquote>p>em')
for elems in products:
    quotes.append(elems.text)

#Books in one line
products = soup.select('p')
elem_list=[]
for elems in products:
    elem_list.append(elems.text)
    
for i in range (len(elem_list)):
    line=elem_list[i]
    if "” —" in line:
        the_book_in_one_sentence.append(elem_list[i+1])

#Why should you read it?
products = soup.select('p')
elem_list=[]
for elems in products:
    elem_list.append(elems.text)
    
for i in range (len(elem_list)):
    line=elem_list[i]
    if "” —" in line:
        why_should_you_read_it.append(elem_list[i+2])


#Key_takeways
products = soup.select('ol')
for elems in products:
    children=elems.children
    children_texts=[]
    for child in children:
        children_texts.append(child.text)
    takeways.append(children_texts)

for t in takeways:
    for i in t:
        if i=="\n":
            t.remove("\n")
        i=i.strip()

for t in takeways:
    if len(t)!=3:
        takeways.remove(t)

for t in takeways:
    takeway_1.append(t[0])
    takeway_2.append(t[1])
    takeway_3.append(t[2])

takeway_1.pop()
takeway_2.pop()
takeway_3.pop()


#Quotes Adjustments Manually

quotes[14]=quotes[14]+quotes[15]
quotes.pop(15)

quotes[16]=quotes[16]+quotes[17]
quotes.pop(17)

quotes[21]=quotes[21]+quotes[22]
quotes.pop(22)

quotes[23]=quotes[23]+quotes[24]
quotes.pop(24)



#the_book_in_one_sentence adjustment
the_book_in_one_sentence.insert(8,"You Are A Badass helps you become self-aware, figure out what you want in life and then summon the guts to not worry about the how, kick others’ opinions to the curb and focus your life on the thing that will make you happy.")
the_book_in_one_sentence.insert(16,"Quiet shows the slow rise of the extrovert ideal for success throughout the 20th century, while making a case for the underappreciated power of introverts and showing up new ways for both forces to cooperate.")
the_book_in_one_sentence.insert(23,"Rich Dad Poor Dad tells the story of a boy with two fathers, one rich, one poor, to help you develop the mindset and financial knowledge you need to build a life of wealth and freedom.")

why_should_you_read_it.insert(23,"As a child, growing up, your views and thoughts are usually shaped by your parents. And in this book, Robert tells the story of how his views about money and how they were shaped by his two dads, one of them being his real father and the other one, his best friend’s father. Money makes the world go round, but how do you deal with them? Read this book to find out.")


#book_edit
book_temp=[]
for b in book:
    pieces = b.split("_")
    book_temp.append(' '.join(map(str, pieces[1:])))

#author seperation
authors=[]
books=[]
for book in book_temp:
    pieces = book.split("by")
    books.append(pieces[0].strip())
    authors.append(pieces[1].strip())
       
for i in range (len(quotes)):
    quote=quotes[i]
    quote.replace("“"," ")
    quotes[i]=quote
    
print(len(books))
print(len(authors))
print(len(quotes))
print(len(the_book_in_one_sentence))
print(len(why_should_you_read_it))
print(len(takeway_1))
print(len(takeway_2))
print(len(takeway_3))



"""
for i in range(33):
    the_book_in_one_sentence[i]=the_book_in_one_sentence[i].replace(",","-")
    why_should_you_read_it[i]=why_should_you_read_it[i].replace(",","-")
    takeway_1[i]=takeway_1[i].replace(",","-")
    takeway_2[i]=takeway_2[i].replace(",","-")
    takeway_3[i]=takeway_3[i].replace(",","-")
    authors[i]=authors[i].replace(",","-")
    books[i]=books[i].replace(",","-")
    quotes[i]=quotes[i].replace(",","-")
"""    
    

data={
    'name':books[:32],
    'authors':authors[:32],
    'Key Takeaway 1':takeway_1,
    'Key Takeaway 2':takeway_2,
    'Key Takeaway 3':takeway_3,
}

df = pd.DataFrame(data)


print (df)

df.to_excel("Data.xlsx")
df.to_csv("data.csv")
