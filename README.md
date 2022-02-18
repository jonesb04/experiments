# Experiments

### URL
- https://downloads.regulations.gov/EPA-HQ-OW-2021-0602-0130/attachment_1.pdf
- https://downloads.regulations.gov/HHSIG-2021-0009-0001/content.pdf

### Create and activate Virtual Environment FIRST
- python3 -m venv .venv
- source .venv/bin/activate

### Install dependices
- brew install poppler
- pip install -r requirements.txt
- if issues installing try installing seperatly
    - pip install requests
    - pip install python-dotenv
    - pip install flask
    - pip install pdftotext
        - if pdftotext has a legacy error and throwing an architecture flag
            - run export ARCHFLAGS="-arch x86_64"

### Create an .env file and add (DON'T HAVE TO DO THIS)
- ATTACHMENT\_URL = the_attachemnt_url
- USERNAME = username_for_regulations_key
- AUTH\_KEY = your_regulations_key

### To run flask server (try running server first through command line before doing this)
- export FLASK_APP=flask_server.py
- export FLASK_ENV=development
- flask run

### Run client in terminal
- run python3 client.py <PDF_URL>