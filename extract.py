import requests
import PyPDF2

pdf = open('EPA-HQ-OW-2021-0602-0130_attachment_1.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdf)
first = pdfReader.getPage(0)
second = pdfReader.getPage(1)
print(first.extractText())
print()
print(second.extractText())

