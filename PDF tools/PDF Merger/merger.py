import os
from PyPDF2 import PdfFileMerger

x=[a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfFileMerger()

for pdf in x:
    merger.append(open(pdf,'rb'))
    print(pdf)

with open ("0000000 - Full Book.pdf","wb") as fout:
    merger.write(fout)
    print("Done")