import os
from flask import Flask

import bp

app = Flask(__name__)
bp.register_blueprints(app)


if __name__ == "__main__":
    host = os.environ['host']
    port = os.environ['port']
    app.run(host, port)