# EXERCISE 8 - MERGE THE PDF
# Problem Statement: Write a program to manipulate pdf files using PyPDF2. Your program should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities. PyPDF2 is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. Pypdf can retrieve text and metadata from PDFs as well.



from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = ["PDF-files\Sample.pdf", "PDF-files\Data-Communication.pdf", "PDF-files\Mens-FTP.pdf"]
for pdf in pdfs:
  merger.append(pdf)

merger.append("PDF-files\MCQs.pdf")

merger.write("Merged-pdf.pdf")
merger.close()