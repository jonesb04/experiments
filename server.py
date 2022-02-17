
from flask import Flask, request
import requests

app = Flask(__name__)

"""
Server receives post request from Client with URL link.
URL is decoded and is sent as a param to save_to_disk()
"""
@app.route('/attachment', methods=['POST'])
def saves_content():
   url = request.get_data()
   save_to_disk(url.decode())
   return url

"""
Writes attachment url to disk.
"""
def save_to_disk(url):
    r = requests.get(url)
    contents = r.content
    # find system to change names of url, with UUID?
    with open("attachment.pdf", 'wb') as f:
        f.write(contents)

# TODO: Add a function that extracts text from the PDF

if __name__ == "__main__":
    app.run()