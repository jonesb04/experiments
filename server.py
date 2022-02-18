
from flask import Flask, request
import requests
import base64
import pdftotext

app = Flask(__name__)

"""
Server receives post request from Client with URL content.
"""
@app.route('/attachment', methods=['POST'])
def saves_content():
    data = request.get_data()
    save_to_disk(data)
    return "Received"

"""
Writes attachment content to disk.
"""
def save_to_disk(data):
    with open("attachment.pdf", 'wb') as f:
        f.write(data)
    extract_pdf_to_txt('attachment.pdf')

def extract_pdf_to_txt(pdf):
    with open(pdf, 'rb') as file:
        txt = pdftotext.PDF(file)

    with open('attachment.txt', 'w') as file:
        for page in txt:
                file.write(page)


if __name__ == "__main__":
    app.run()