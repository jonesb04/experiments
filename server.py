
from flask import Flask, request
import requests
import base64

app = Flask(__name__)

"""
Server receives post request from Client with URL link.
URL is decoded and is sent as a param to save_to_disk()
"""
@app.route('/attachment', methods=['POST'])
def saves_content():
    data = request.get_data()
    # print(data, type(data))
    save_to_disk(data)
    return "Received"

"""
Writes attachment url to disk.
"""
def save_to_disk(data):
    with open("attachment5.pdf", 'wb') as f:
        f.write(data)

# TODO: Add a function that extracts text from the PDF

if __name__ == "__main__":
    app.run()