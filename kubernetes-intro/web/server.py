from datetime import datetime
from flask import Flask, current_app

app = Flask(__name__, static_folder="/app")

@app.route('/<string:page_name>')
def home(page_name):
    return current_app.send_static_file(page_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
