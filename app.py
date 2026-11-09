
from flask import Flask, jsonify
from pymongo import MongoClient, DESCENDING
from dotenv import load_dotenv
import os
import time
import logging

# Load environment variables
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# MongoDB connection
client = MongoClient(
    os.getenv("MONGO_URI"),
    serverSelectionTimeoutMS=5000
)

db = client[os.getenv("DATABASE_NAME", "activity_db")]
collection = db[os.getenv("COLLECTION_NAME", "activity_logs")]


# Check MongoDB connection
try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")
except Exception as error:
    print("MongoDB connection failed:", error)


# API: Get the latest 10 activity logs
@app.route("/logs/recent", methods=["GET"])
def recent_logs():

    # Start measuring response time
    start_time = time.perf_counter()

    try:
        # Fetch latest 10 documents
        documents = list(
            collection.find()
            .sort("timestamp", DESCENDING)
            .limit(10)
        )

        # Convert MongoDB ObjectId to string
        for document in documents:
            document["_id"] = str(document["_id"])

        # Return JSON response
        response = jsonify(documents)

        return response

    except Exception:
        app.logger.exception("Error fetching activity logs")
        return jsonify({
            "error": "Unable to fetch activity logs"
        }), 500

    finally:
        # Calculate and log response time
        end_time = time.perf_counter()
        response_time = (end_time - start_time) * 1000

        app.logger.info(
            "Recent logs API response time: %.2f ms",
            response_time
        )


# Run Flask application
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.getenv("PORT", 5000)),
        debug=False
    )
