import os

from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def hello_world():
    return 'Ping'


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000))
