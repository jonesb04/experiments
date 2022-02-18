# experiments

### URL
https://downloads.regulations.gov/EPA-HQ-OW-2021-0602-0130/attachment_1.pdf

### Create and activate Virtual Environment FIRST
- python3 -m venv .venv
- source .venv/bin/activate

### Install dependices
- pip install requests
- pip install python-dotenv
- pip install flask
- brew install poppler
- pip install pdftotext

### Create an .env file and add (DON'T HAVE TO DO THIS)
- ATTACHMENT\_URL = the_attachemnt_url
- USERNAME = username_for_regulations_key
- AUTH\_KEY = your_regulations_key

### To run flask server (try running server first through command line before doing this)
- export FLASK_APP=flask_server.py
- export FLASK_ENV=development
- flask run
