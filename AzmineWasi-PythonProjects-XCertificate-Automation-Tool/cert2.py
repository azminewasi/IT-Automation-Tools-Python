from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import cv2

form = pd.read_excel("Attendees.xlsx")
name_list = form['Name'].to_list()
mail_list = form['Mail'].to_list()


img = cv2.imread('cert.png')
MAX_H,MAX_W,r = img.shape
current_h, pad = (MAX_H/2)-30, 10

print(img.shape)
total = len(name_list)
ei=0
while (ei<total):
	i=name_list[ei]
	filenamess=mail_list[ei]+".png"
	if (len(i)>35):
		font = ImageFont.truetype("OLD.ttf", 40)
		current_h, pad = (MAX_H/2), 10
	elif (len(i)>25):
		font = ImageFont.truetype("OLD.ttf", 55)
	elif (len(i)>20):
		font = ImageFont.truetype("OLD.ttf", 72)
	else:
		font = ImageFont.truetype("OLD.ttf", 80)


	im = Image.open("cert.png")
	d = ImageDraw.Draw(im)
	w, h = d.textsize(i, font=font)
	location = ((MAX_W - w) / 2, current_h)
	text_color = (16,37,68)
	d.text(location, i, fill=text_color,font=font)
	im.save("files/"+filenamess)
	print(i, "----- Done---  ",filenamess,"--", ei)
	ei=ei+1