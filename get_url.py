import requests

file_url = "https://downloads.regulations.gov/EPA-HQ-OW-2021-0602-0130/attachment_1.pdf"
r = requests.get(file_url)
r.encoding = 'utf-8'

print(r.text)

