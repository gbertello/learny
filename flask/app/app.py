from flask import Flask, jsonify, request
from flask_cors import CORS


application = Flask(__name__)
application.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
CORS(application)


@application.route('/')
def index():
  return jsonify({"message": "Hello, World!"})
  
  
if __name__ == "__main__":
  application.run()
