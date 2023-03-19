from fpdf import FPDF
from PIL import Image
import glob
import os


# set here
image_directory = ''
extensions = ('*.jpg','*.png','*.jpeg') #add your image extentions
# set 0 if you want to fit pdf to image
# unit : pt
margin = 0

imagelist=["Dataset Obsevation.png"]

for imagePath in imagelist:
    cover = Image.open(imagePath)
    width, height = cover.size
    
pdf = FPDF(unit="pt", format=[width + margin, height + margin])
for imagePath in imagelist:
    pdf.add_page()
    
    pdf.image(imagePath, margin, margin)

pdf.output("data" + ".pdf", "F")