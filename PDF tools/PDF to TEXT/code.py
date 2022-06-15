import PyPDF2

pdfFileObj=open('xyz.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
print("Total Pages: ",pdfReader.numPages)


for i in range(3):
	print("\nPage",i+1,"\n\n\n")
	pageObj=pdfReader.getPage(i)
	print(pageObj.extractText())
	if (len(pageObj.extractText())==0):
		print("No data")

pdfFileObj.close()