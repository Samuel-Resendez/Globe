#Author: Samuel Resendez



from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import tornado.websocket as ws


import eventlet
from flask import Flask, render_template
from flask_ask import Ask, statement, question
from geopy.geocoders import GoogleV3
from flask_socketio import SocketIO, send, emit


""" Setting Global Vars """
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode='eventlet')


ask = Ask(app, '/')
geo_locator = GoogleV3(api_key="AIzaSyC0q7QFF35WNbYWvr4hdFrlsr6RUCGYLRw")
data_sets = []
user_id = 0


### Initialization Functions ###

@ask.launch
def new_connection():
    """Called upon initialization"""
    # r = requests.get(url)


    return question("Hello, welcome to Globe, what would you like to see today?")



@app.route("/")
def initialize():
    return render_template('index.html',async_mode='eventlet')

### TRAVEL FUNCTIONS ###




@ask.intent('goToDestinationIntent')
def travel_to_location(location):
    """Called to move to another location on the map. Should set up a websocket with react thingy"""
    # location is name of location

    print(location)

    loc_obj = geo_locator.geocode(location)

    print(loc_obj.latitude, end=', ')
    print(loc_obj.longitude)

    # start websocket
    send()
    text = render_template('viewLocation', latitute=int(loc_obj.latitude), longitude=int(loc_obj.longitude), location=location)

    return question(text)


@ask.intent('zoomInIntent')
def zoom_in():

    # make post request/update webapp

    text = render_template('zoomIn')

    return question(text)

@ask.intent('zoomOutIntent')
def zoom_out():

    text = render_template('zoomOut')

    return question(text)


@ask.intent('quitIntent')
def quit_map():

    return statement("Thank you for using globe, goodbye!")


### DATA PREFERENCE FUNCTIONS ###



### SOCKET POST FUNCTION ###

@socketio.on('join', namespace='/sock')
def join(message):

    print("We are connected!")
    print(message)




### WEBSOCKET CLASSES ###
class EchoWebSocket(ws.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")



### CONFIG FUNCTIONS ###

@ask.intent('testAlexaIntent')
def hello_world():

    return statement("Hello World!")



if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    print("Starting server...")
    IOLoop.instance().start()
