from fpdf import FPDF
from PIL import Image
import glob
import os


# set here
image_directory = ''
extensions = ('*.jpg','*.png','*.jpeg','*.JPG','*.JPEG','*.PNG') #add your image extentions
# set 0 if you want to fit pdf to image
# unit : pt
margin = 0

import glob

# Define the list of extensions
extensions = ('*.jpg', '*.png', '*.jpeg', '*.JPG', '*.JPEG', '*.PNG')
file_list = []
# Create a list to store the filenames
for ext in extensions:
    file_list.extend(glob.glob(ext))

imagelist=file_list

for imagePath in imagelist:
    cover = Image.open(imagePath)
    width, height = cover.size
    
pdf = FPDF(unit="pt", format=[width + margin, height + margin])
for imagePath in imagelist:
    pdf.add_page()
    
    pdf.image(imagePath, margin, margin)

pdf.output("data" + ".pdf", "F")