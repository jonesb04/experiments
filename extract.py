"""
The following installations must be made in the terminal in order for the program to work:
    brew install poppler
    pip install pdftotext
"""
import requests
import pdftotext

with open('EPA-HQ-OW-2021-0602-0130_attachment_1.pdf', 'rb') as file:
    pdf = pdftotext.PDF(file)

with open('PDF_As_Text.txt', 'w') as file:
    for page in pdf:
            file.write(page)
