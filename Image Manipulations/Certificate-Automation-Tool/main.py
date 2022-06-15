from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import cv2
import os



excel_file_name="Data.xlsx" 
height_adjustment=30
font_name="FONT.otf"
text_color = (16,37,68)
cert_demo="cert.png"

fontXLtext=ImageFont.truetype(font_name, 40)
fontLtext=ImageFont.truetype(font_name, 55)
fontMtext=ImageFont.truetype(font_name, 72)
fontNtext=ImageFont.truetype(font_name, 80)



form = pd.read_excel(excel_file_name)
name_list = form['Name'].to_list()
mail_list = form['Mail'].to_list()

img = cv2.imread(cert_demo)
MAX_H,MAX_W,r = img.shape
current_h, pad = (MAX_H/2)-height_adjustment, 10

os.mkdir("pdfs")
os.mkdir("pngs")

print(img.shape)
total = len(name_list)
count=0
while (count<total):
    i=name_list[count]
    if (len(i)>35):
        font = fontXLtext
    elif (len(i)>25):
        font = fontLtext
    elif (len(i)>20):
        font = fontMtext
    else:
        font = fontNtext
        
    im = Image.open(cert_demo)
    d = ImageDraw.Draw(im)
    w, h = d.textsize(i, font=font)
    location = ((MAX_W - w) / 2, current_h)
    d.text(location, i, fill=text_color,font=font)
    im.save("pngs/"+mail_list[count]+".png")
    im.save("pdfs/"+mail_list[count]+".pdf")
    print(count+1,i, "----- Done---  ",mail_list[count])
    count=count+1