from flask import Flask, request
from flask_cors import CORS
from flask.json import jsonify

#CREANDO API
app = Flask(__name__)
cors = CORS(app)






if __name__ == "__main__":
    app.run(host="localhost", port="4000", debug=True)