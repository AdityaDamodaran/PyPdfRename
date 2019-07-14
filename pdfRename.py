import pyPdf
import sys
import os
for filename in os.listdir(sys.argv[1]):
	if filename.endswith(".pdf"):
		filepath = sys.argv[1]+filename
		pdf = pyPdf.PdfFileReader(file(filepath,"rb"))
		title = pdf.getPage(0).extractText()[:40]
		confirmation = raw_input(filepath+": I think the title of this file is: '" + title +"'. Rename? (y/n)")
		if(confirmation=="y"):
			print filepath
#stripslashes
			print os.path.join(os.path.dirname(filepath),title+".pdf") 
			os.rename(filepath,os.path.join(os.path.dirname(filepath),title+".pdf"))


