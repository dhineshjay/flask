from flask import Flask, redirect  # Added redirect
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the /htop route
    return redirect('/htop')

@app.route('/htop')
def htop():
    full_name = "Dhinesh"
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S %Z")
    top_output = subprocess.getoutput('top -n 1 -b')

    # Build the response line by line
    response_lines = [
        f"Name: {full_name}",
        f"Username: {username}",
        f"Server Time (IST): {server_time}",
        "TOP Output:",
        top_output
    ]

    # Join the lines with line breaks
    response_text = "\n".join(response_lines)

    # Return the response as plain text
    return f"<pre>{response_text}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
