from __future__ import print_function
import os
import subprocess

x=[a for a in os.listdir() if a.endswith(".pdf")]

for file in x:
    if file.endswith(".pdf"):
        filename = file
        print (filename)
        arg1= '-sOutputFile='+str(x.index(file))+"dd.pdf"
        print (arg1)
        p = subprocess.Popen(['C:/Program Files/gs/gs9.55.0/bin/gswin64c.exe',
                              '-sDEVICE=pdfwrite', 
                              '-dCompatibilityLevel=1.4', 
                              '-dPDFSETTINGS=/screen', '-dNOPAUSE', 
                              '-dBATCH', '-dQUIET', str(arg1), filename], 
                             stdout=subprocess.PIPE)
        print (p.communicate())