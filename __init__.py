from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS module
import sqlite3

import logging, ngrok
#ngrok.set_auth_token('1cNqEp7tP9MweFlplGCfrWZp8aL_6hsJibyMvUmednY1LFQq4')
logging.basicConfig(level=logging.INFO)
listener = ngrok.werkzeug_develop()


app = Flask(__name__)
CORS(app)  # Initialize CORS extension with your Flask app

# Function to establish connection to SQLite database
def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

# Endpoint to get data from the database
@app.route('/api/asin', methods=['GET'])
def get_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')
    data = cursor.fetchall()
    asin_list = []
    for row in data:
        asin_list.append(row[1])
    conn.close()
    return jsonify(asin_list)

if __name__ == '__main__':
    app.run(debug=True)
