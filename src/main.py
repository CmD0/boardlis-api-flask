import mongoengine as me
import os
from flask import Flask
from flask_cors import CORS

import bp

app = Flask(__name__)
bp.register_blueprints(app)
CORS(app)


if __name__ == "__main__":
    
    user = os.environ.get('mongoUser')
    password = os.environ.get('mongoPass')
    me.connection.connect("main", host=f"mongodb+srv://{user}:{password}@boardlis-main.wtrgj5g.mongodb.net/?retryWrites=true&w=majority")
    
    host = os.environ.get('host')
    port = os.environ.get('port')
    app.run(host, port)