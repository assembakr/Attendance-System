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

### 4. Enjoy the Application:
- The ```app.py``` file manages all app pages.
- Start enjoying the grocery shop application!
