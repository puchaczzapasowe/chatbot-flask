from flask import Flask, render_template,request
import json
from chat import get_response
from flask_cors import CORS
from flask_socketio import SocketIO
from markupsafe import escape
import sqlite3
app = Flask(__name__)
socketIO = SocketIO(app)

# Enable CORS
CORS(app, origins='http://localhost:5173')
@app.route('/')
def index():
    conn = sqlite3.connect('./static/projektAI.db')
    cursor = conn.cursor()
    tables = cursor.fetchall()


    for table in tables:
        print(table[0])
    return json.dumps({"message":"dziala"})


@app.route('/bot', methods=['POST'])
def handleBotMessage():
    message = request.get_json()
    message["message"]
    return get_response(message["message"])
