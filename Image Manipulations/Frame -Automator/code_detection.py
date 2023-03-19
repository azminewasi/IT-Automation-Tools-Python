from PIL import Image, ImageDraw, ImageFont, ImageOps
import pandas as pd
import cv2
import time

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
failed=[]

def detect(gray, frame):
	faces=face_cascade.detectMultiScale(gray,1.5,5)
	for (x,y,w,h) in faces:
		data=[x,y,w,h]
		return data

def face_location_processing (h,w,data,img,name):

	
	f_x=data[0]+data[2]/4
	f_y=data[1]+data[3]/4
	f_h=data[3]
	f_w=data[2]



	if f_h>f_w:
		f_h=f_h+(h*0.25)
		if f_h>h:
			f_h=h
	f_w=f_h

	if f_w>f_h:
		f_w=f_w+(w*0.25)
		if f_w>w:
			f_w=w
	f_h=f_w

	

	crop_img = img[int(f_y-(f_h/2)):int(f_y+f_h), int(f_x-(f_w/2)):int(f_x+f_w)]
	cv2.imwrite("auto_cropped/"+name, crop_img)
	return crop_img


form = pd.read_excel("Database - Copy.xlsx")
name_list = form['Name'].to_list()
email_list=form['University'].to_list()
id_list=form['Code'].to_list()
uni_list=form['University'].to_list()

total = len(name_list)
ei=0
while (ei<total):
	i=name_list[ei]
	uni_name=uni_list[ei]
	photolocation=r"Pic/"+id_list[ei]+".png"
	print("Currently loading... :",id_list[ei])


	filenamess=name_list[ei].strip()+" - "+email_list[ei].strip()+".png"

	font = ImageFont.truetype("BwGlennSansDEMO-ExtraBold.otf", 88)
	font2 = ImageFont.truetype("BwGlennSansDEMO-LightItalic.otf", 58)



	im = Image.open("best 2.png")

	imgData=cv2.imread(r"Pic/"+id_list[ei]+".png")

	if type(imgData)==type(None):
		print("Image loading Failed")
		ei=ei+1
		failed.append(str(id_list[ei])+"  -  Image loading Failed")
		continue

	i_height, i_width, i_channels = imgData.shape
	print("Image Size: "+str(i_height)+"x"+str(i_width))

	gray=cv2.cvtColor(imgData, cv2.COLOR_BGR2GRAY)
	canvas_data=detect(gray,imgData)

	if canvas_data==None:
		print("Face detection Failed")
		ei=ei+1
		failed.append(str(id_list[ei])+"  -  Face detection Failed")
		continue


	MAX_H,MAX_W = 2083,2088
	current_h, pad = 1390, 5

	person=face_location_processing (i_height, i_width,canvas_data,imgData,id_list[ei]+".png")


	d = ImageDraw.Draw(im)
	w, h = d.textsize(i, font=font)
	location = ((MAX_W - w) / 2, current_h)
	text_color = (0,0,0)
	d.text(location, i, fill=text_color,font=font)


	MAX_H2,MAX_W2 = 2083,2088
	current_h2, pad2 = 1570, 5

	d2 = ImageDraw.Draw(im)
	w2, h2 = d2.textsize(uni_name, font=font2)
	location2 = ((MAX_W2 - w2) / 2, current_h2)
	text_color = (256,256,256)
	d2.text(location2, uni_name, fill=text_color,font=font2)



	color_coverted = cv2.cvtColor(person, cv2.COLOR_BGR2RGB)
	person = Image.fromarray(color_coverted)

	person = person.resize((480,480), Image.ANTIALIAS)
	
	bigsize = (person.size[0], person.size[1])
	mask = Image.new('L', bigsize, 0)
	draw = ImageDraw.Draw(mask) 
	draw.ellipse((0, 0) + bigsize, fill=255)
	mask = mask.resize(person.size, Image.ANTIALIAS)
	person.putalpha(mask)
	

	#im.paste(person, (375, 330))
	im=im.resize(im.size,Image.ANTIALIAS)
	

	saveimg = Image.new('RGB', im.size, color = 'white')
	saveimg.paste(im,(0,0))
	saveimg.paste(person, (810,303),person)

	saveimg.save("files/"+filenamess)
	print(ei+1,"--", i, "----- Done---  ",filenamess)

	pdfimg=saveimg.convert('RGB')
	pdfimg.save("pdf_files/"+filenamess.replace("png","pdf"))
	ei=ei+1

for file in failed:
	print(file)