
import pandas as pd
import cv2
import random
import string

form = pd.read_excel("DATA.xlsx")
name_list = form['Name'].to_list()

def replacer(txt):
	txt=txt.replace("a","b")

total = len(name_list)
letters = string.ascii_lowercase
number="1234567890"
ei=int(0)
f=open("datax.txt","w")
while (ei<total):
	print("Writing",name_list[ei])
	f.write("Full Name:{data}\n".format(data=''.join(random.choice(letters+" ") for i in range(12))))
	f.write("Father's Name:{data}\n".format(data=''.join(random.choice(letters+" ") for i in range(14))))
	f.write("Mother's Name:{data}\n".format(data=''.join(random.choice(letters+" ") for i in range(15))))
	f.write("Blood Group:{data}\n".format(data=''.join(random.choice(letters) for i in range(1))+"+"))
	f.write("Home District:{data}\n".format(data=''.join(random.choice(letters) for i in range(6))))
	f.write("Current Address:{data}\n".format(data=''.join(random.choice(letters+", ") for i in range(20))))
	f.write("Institution:{data}\n".format(data=''.join(random.choice(letters) for i in range(20))))
	f.write("Department:{data}\n".format(data=''.join(random.choice(letters) for i in range(4))))
	f.write("Year:{data}\n".format(data=''.join(random.choice(number) for i in range(1))))
	f.write("Contact Number:{data}\n".format(data=''.join(random.choice(letters) for i in range(10))))
	f.write("Email:{data}\n".format(data=''.join(random.choice(letters) for i in range(5))+"@gmail.com"))
	f.write("Code:{data}\n".format(data=''.join(random.choice(letters) for i in range(2))))
	f.write("\n\n")
	
	



	ei=ei+1