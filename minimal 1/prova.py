from flask import Flask
from flask import request

# Create our flask app. Static files are served from 'static' directory
app = Flask(__name__)

@app.route('/')
def entry():
    print('hello world!')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)