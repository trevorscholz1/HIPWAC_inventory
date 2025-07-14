# HIPWAC Inventory Search

This program is apart of the efforts to catalogue the lab and improve lab organization.
It searches the catalogue using natural lanuage to return best matches and point the user to
which drybox/drawer the item can be found.
You can run it either as a web app or as a command-line tool (see below).

---

## Requirements

- Python 3.10+ recommended
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

    cd path/to/your/project

3.  Create a virtual environment using Python 3.10:

        python3.10 -m venv venv

4.  Activate the virtual environment:

        source venv/bin/activate

5.  Install dependencies:

    pip install -r requirements.txt (should start listing all of the installations, might take a minute)

---

## Inventory File

Make sure there is a file named inventory.csv in the same folder, I will continue to update the inventory as we make changes to the google sheet.

The columns should be: - object - size - brand - drybox

---

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

- This app uses a pre-trained model from SentenceTransformers: 'all-MiniLM-L6-v2'
- Will continue tp update as we keep cataloging the lab.
- Let Trevor know of any errors, suggested edits, etc.
- Right now the search takes a little longer than I want, might experiment with the models from SentenceTransformers
