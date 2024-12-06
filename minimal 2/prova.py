from flask import Flask
from flask import request

# Create our flask app. Static files are served from 'static' directory
app = Flask(__name__)

# this route simply serves 'static/index.html'
@app.route('/user')
def index():
    return app.send_static_file('user.html')

@app.route('/station/<int:station_id>')
def station(station_id):
# show the station with the given id, the id is an integer
    return f'Retrieving info for Station: {station_id}'

@app.route('/')
def entry():
    user_agent = request.headers.get('User-Agent')

    return '<p>Your current browser is {}</p>'.format(user_agent)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)