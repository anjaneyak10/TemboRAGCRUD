import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from api import controller

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.register_blueprint(controller)
load_dotenv()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9083)





