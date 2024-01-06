# Students-Attendance-System

## Project Overview

A computer vision-based project designed to recognize and identify individuals based on their facial features. The system utilizes state-of-the-art deep learning and image processing techniques to real-time face recognition. It is deployed using a Flask web application to facilitate attendance tracking through a Google Sheets spreadsheet.

## Running the Project
  
### 1. Clone this Repo:
  ```
  git clone https://github.com/MariamAmy/Students-Attendance-System
  ```


### 2. Install the required dependencies:
  ```python
  pip install -r requirements.txt
  ```


### 3. Hosting the Application
To host the application and make it accessible online, we used ngrok. Follow the steps below:
- Install ngrok:
  ```
  npm install ngrok -g
  ```
- Run the Flask  application:
  ```
  python app.py
  ```
- In a separate terminal, run ngrok to expose the local server:
  ```
  ngrok http 5000
  ```

### 4. Access the Application:
- Once you have hosted the application using ngrok, you will receive a public URL.
- Open your web browser and navigate to the provided ngrok URL.

### 5. Utilize the Attendance System:
- The application interface will guide you through the attendance tracking process.
- Upload an image.
- The system will identify individuals and update the attendance records in the Google Sheets spreadsheet.

### 6. Monitor Attendance:
- Access the Google Sheets spreadsheet to view the real-time attendance data.
- The spreadsheet is automatically updated as students are recognized by the system.

### Feel free to contribute to the project by submitting pull requests or reporting issues!

