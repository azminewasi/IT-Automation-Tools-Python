from fpdf import FPDF
from PIL import Image
import glob
import os


# set here
image_directory = ''
extensions = ('*.jpg','*.png','*.gif') #add your image extentions
# set 0 if you want to fit pdf to image
# unit : pt
margin = 10

imagelist=[]
for ext in extensions:
    imagelist.extend(glob.glob(os.path.join(image_directory,ext)))

for imagePath in imagelist:
    cover = Image.open(imagePath)
    width, height = cover.size
pdf = FPDF(unit="pt", format=[width + 2*margin, height + 2*margin])
for imagePath in imagelist:
    pdf.add_page()
    pdf.image(imagePath, margin, margin)

pdf.output("data" + ".pdf", "F")