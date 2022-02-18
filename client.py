'''
Allows clients to save 

Comments with attachments are not saved, with this (c_Attachemnt) we can finally get what the real attachments are

Does the URL have to be the actual pdf or a link to a comment, scraping the pdf?
- No just take attachment URL's
'''

import requests
import argparse

class Client():

    def __init__(self, attachment_url, server_url):
        self.attachment_url = attachment_url
        attach_requests = requests.get(attachment_url.URL, " ")
        self.server_url = server_url
        # Needs to check if this works for other files, future testing note
        self.content = attach_requests.content

    # This function saves the pdf to disk from the url
    def save_to_disk(self):
        with open(self.file_name, 'wb') as f:
            f.write(self.content)

    # This function send the attachment url to the server
    def send_data(self):
        # Have to make sure encodings are always bytes represented, future testing note
        requests.post(self.server_url + "/attachment", data=self.content)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Input URL to be downloaded.")
    parser.add_argument("URL")
    attachment_url = parser.parse_args()
    client = Client(attachment_url, "http://127.0.0.1:5000")
    client.send_data()