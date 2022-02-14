import requests
import pdftotext

with open('EPA-HQ-OW-2021-0602-0130_attachment_1.pdf', 'rb') as f:
    pdf = pdftotext.PDF(f)

for page in pdf:
    print(page)

#with open('extracted.txt', 'w') as f:
 #  f.write(first)
  # f.write('\n')
  # f.write(second)


