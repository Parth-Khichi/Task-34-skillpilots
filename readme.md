Activity Logs API

A simple Flask REST API that fetches the latest 10 activity documents from MongoDB, sorts them by timestamp, and returns them as JSON.

1. Project Structure
text
activity_logs_api/
│
├── app.py
├── requirements.txt
├── .env
└── README.md

2. Technologies Used
Python
Flask
MongoDB
PyMongo
Python-dotenv
3. Requirements

Make sure you have installed:

Python 3
MongoDB
pip
4. Installation

Open your terminal and navigate to the project folder.

bash
cd activity_logs_api


Create a virtual environment:

bash
python -m venv venv


Activate the virtual environment.

Windows:

bash
venv\Scripts\activate


Mac/Linux:

bash
source venv/bin/activate


Install the required packages:

bash
pip install -r requirements.txt

5. Environment Configuration

Create a .env file:

env
MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=activity_db
COLLECTION_NAME=activity_logs
PORT=5000


Make sure MongoDB is running before starting the application.

6. Run the Project

Start the Flask application:

bash
python app.py


The application will run at:

text
http://127.0.0.1:5000

7. API Endpoint
Get Recent Activity Logs
URL: /logs/recent
Method: GET
Description: Returns the latest 10 activity documents sorted by timestamp in descending order.

Example:

text
http://127.0.0.1:5000/logs/recent

8. Add Sample Data

Open MongoDB Shell and execute:

javascript
use activity_db

db.activity_logs.insertMany([
  {
    action: "User Login",
    username: "John",
    timestamp: new Date()
  },
  {
    action: "File Uploaded",
    username: "Alex",
    timestamp: new Date()
  },
  {
    action: "User Logout",
    username: "David",
    timestamp: new Date()
  }
])

9. Test Using cURL

Run this command in another terminal:

bash
curl http://127.0.0.1:5000/logs/recent


The API returns a JSON array containing the latest 10 activity documents.

10. Measure Response Time

Use this command to measure API response time:

bash
curl -o /dev/null -s -w "Response Time: %{time_total} seconds\n" http://127.0.0.1:5000/logs/recent


For Windows CMD:

bash
curl -o NUL -s -w "Response Time: %{time_total} seconds\n" http://127.0.0.1:5000/logs/recent


The Flask terminal also displays response-time logs in milliseconds.

11. Expected Result

The API returns a JSON response similar to:

json
[
  {
    "_id": "672a12345678901234567890",
    "action": "User Login",
    "username": "John",
    "timestamp": "2026-11-09T09:00:00Z"
  }
]


The actual response depends on the documents stored in MongoDB.

12. Features
Simple Flask REST API.
Fetches the latest 10 activity documents.
Sorts documents by timestamp (newest first).
Returns data in JSON format.
Measures API response time.
Logs performance information.
Handles database errors.
13. Conclusion

This project implements a simple Flask API to retrieve recent activity logs from MongoDB. It also measures and logs response time, as required by the task.