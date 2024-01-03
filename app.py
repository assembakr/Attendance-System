from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import pickle
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils import face_encodings, nb_of_matches
from datetime import date
from student_dictionary import students

app = Flask(__name__)

# Load the encodings + names dictionary
with open("encodings.pickle", "rb") as f:
    name_encodings_dict = pickle.load(f)

# Set up Google Sheets credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("attendance-410016-aab114cb5a63.json", scope)
client = gspread.authorize(creds)

def create_or_get_sheet():
    workbook_name = "Attendance Project"
    today_date = date.today().strftime("%Y-%m-%d")
    try:
        # Try to get the workbook
        workbook = client.open(workbook_name)
    except gspread.exceptions.SpreadsheetNotFound:
        # If the workbook does not exist, create it
        workbook = client.create(workbook_name)

        workbook.share("", perm_type="anyone", role="writer", notify=False)

    try:
        # Try to get the sheet for today
        sheet = workbook.worksheet(today_date)
    except gspread.exceptions.WorksheetNotFound:
        # If the sheet for today does not exist, create a new one
        sheet = workbook.add_worksheet(today_date, 1, 2)  # Added 2 columns for IDs and Names

        # Set the header row
        sheet.update_cell(1, 1, "IDs")
        sheet.update_cell(1, 2, "Names")

    return sheet, workbook.url

def recognize_faces(image, existing_ids):
    encodings = face_encodings(image)
    ids = []
    names = []

    for encoding in encodings:
        counts = {}
        for (id, encodings) in name_encodings_dict.items():
            counts[id] = nb_of_matches(encodings, encoding)

        if all(count == 0 for count in counts.values()):
            id = "Unknown"
            name = "Unknown"
        else:
            id = max(counts, key=counts.get)
            name = students.get(id, "Unknown")

        if id not in existing_ids:
            ids.append(id)
            names.append(name)
            existing_ids.add(id)

    return ids, names

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Get existing IDs from the sheet
        sheet, _ = create_or_get_sheet()
        existing_ids = set(sheet.col_values(1))  # Assuming IDs are in the first column

        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        detected_ids, detected_names = recognize_faces(image, existing_ids)

        # Write the detected IDs and Names to Google Sheets
        sheet, worksheet_url = create_or_get_sheet()
        df = pd.DataFrame({"IDs": detected_ids, "Names": detected_names})
        sheet.append_rows(df.values.tolist(), value_input_option='RAW')

        return render_template('result.html', ids_names=zip(detected_ids, detected_names), worksheet_url=worksheet_url)

if __name__ == '__main__':
    app.run(debug=True)