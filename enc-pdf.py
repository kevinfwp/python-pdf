import PyPDF2
import os

file="pdf-file.pdf"
pdf_obj=open(file,'rb')
pdf_reader=PyPDF2.PdfFileReader(pdf_obj)
pdf_writer=PyPDF2.PdfFileWriter()
for page_num in range(pdf_reader.numPages): 
  print(page_num)
  page_obj=pdf_reader.getPage(page_num)
  pdf_writer.addPage(page_obj)
pdf_writer.encrypt('pass')
pdf_output_file=open(file.split(".")[0]+"_sec.pdf",'wb') 
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
