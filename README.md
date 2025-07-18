# HIPWAC Inventory Search

This program is a part of the efforts to catalogue the lab and improve lab organization.
It searches the catalogue using natural lanuage to return best matches and point the user to
which drybox/drawer the item can be found.

You can run it either as a web app or as a command-line tool (see below).

The "Score" next to each result is a score of how well the item matched the search query.

---

## Requirements

- Python 3.10 (this is just the version I used, really any modern version should work)
- pip

All required Python packages are listed in requirements.txt:
flask
pandas
torch
sentence-transformers

---

## Setup Instructions with a venv (assuming MacOS)

1.  Open your terminal

2.  Navigate to the project folder:

    cd path/to/your/project (For example, for me it is cd Documents/catalogue_search)

3.  Create a virtual environment using Python 3.10:

        python3.10 -m venv venv

4.  Activate the virtual environment:

        source venv/bin/activate

5.  Install dependencies:

    pip install -r requirements.txt (should start listing all of the installations, might take a minute)

---

## Inventory File

I am currently hosting the inventory file instead of having it in this project locally to allow
for updates to the inventory without having to update the local version of it.

---

## Activate the venv (if you have not already)

source venv/bin/activate

## Running the Web App (has a nice UI so recommended)

To start the Flask server:

    python app.py

Then open your browser and go to:

    http://127.0.0.1:5000/

---

## Running from the Command Line

To search directly from the terminal:

    python app.py -"your search term here"

Example:

    python app.py -"Off axis parabolas"

You'll see the top 5 matches printed in your terminal.

---

## Notes

- I used a pre-trained model from SentenceTransformers: 'all-MiniLM-L6-v2'
- Will continue tp update as we keep cataloging the lab.
- Let me know of any errors, suggested edits, etc.
- Right now the search takes a little longer than I want, might experiment with the models from SentenceTransformers
