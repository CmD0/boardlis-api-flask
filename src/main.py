import mongoengine as me
import os
from flask import Flask

import bp

app = Flask(__name__)
bp.register_blueprints(app)


if __name__ == "__main__":
    
    user = os.environ['mongoUser']
    password = os.environ['mongoPass']
    me.connection.connect("main", host=f"mongodb+srv://{user}:{password}@boardlis-main.wtrgj5g.mongodb.net/?retryWrites=true&w=majority")
    
    host = os.environ['host']
    port = os.environ['port']
    app.run(host, port)