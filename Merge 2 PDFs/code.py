from PyPDF2 import PdfFileReader,PdfFileMerger

f1=PdfFileReader("name")
f2=PdfFileReader("name")
out=PdfFileMerger()
out.append(f1)
out.append(f2)
out.write(name)