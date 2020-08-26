import glob
import fitz
import os

def pic2pdf():
    doc = fitz.open()
    for img in sorted(glob.glob("*.png")):
        imgdoc = fitz.open(img)                 
        pdfbytes = imgdoc.convertToPDF()       
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                 
    if os.path.exists("allimages-01.pdf"):
        os.remove("allimages-01.pdf")
    doc.save("allimages-01.pdf")                
    doc.close()

if __name__ == '__main__':
    pic2pdf()
