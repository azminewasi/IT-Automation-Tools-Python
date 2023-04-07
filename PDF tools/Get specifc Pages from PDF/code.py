from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2
import os

pdfReader = PdfFileReader("Statistical Quality Control by Montgomery .pdf")
savepath='./'
information = [("Statistical Quality Control by Montgomery .pdf",718,718)]

for page in range(len(information)):
    pdf_writer = PyPDF2.PdfFileWriter()
    start = information[page][1]
    end = information[page][2]
    while start<=end:
        pdf_writer.addPage(pdfReader.getPage(start-1))
        start+=1
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    output_filename = '{}_{}_page_{}.pdf'.format(information[page][0],information[page][1], information[page][2])
    with open(output_filename,'wb') as out:
        pdf_writer.write(out)