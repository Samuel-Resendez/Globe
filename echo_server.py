#Author: Samuel Resendez




from flask import Flask, render_template
from flask_ask import Ask, statement, question
from geopy.geocoders import GoogleV3
import requests


""" Setting Global Vars """
app = Flask(__name__)


ask = Ask(app, '/')
geo_locator = GoogleV3(api_key="AIzaSyC0q7QFF35WNbYWvr4hdFrlsr6RUCGYLRw")
data_sets = ["meteor strikes","plane crashes","drone strikes","police killings"]
user_id = 0



### Initialization Functions ###

@ask.launch
def new_connection():
    """Called upon initialization"""
    # r = requests.get(url)


    return question("Welcome, setting up your connection to Globe?")



@app.route("/")
def initialize():
    return render_template('index.html')

### TRAVEL FUNCTIONS ###




@ask.intent('goToDestinationIntent')
def travel_to_location(location):
    """Called to move to another location on the map. Should set up a websocket with react thingy"""
    # location is name of location

    print(location)
    try:
        loc_obj = geo_locator.geocode(location)
        url = "https://globe-sb.herokuapp.com/"
        r = requests.post(url, data= {'longitude': loc_obj.longitude,'latitude':loc_obj.latitude})
        # start websocket
        print(r.status_code)
        if r.status_code == 200:
            text = render_template('viewLocation',location=location)

            return question(text)
    except Exception as e:
        return question("Request failed. Please try again")


@ask.intent('zoomInIntent')
def zoom_in():

    # make post request/update webapp
    url = "https://globe-sb.herokuapp.com/alexaPosition"
    try:
        r = requests.post(url, data={"zoom_delta":-3})
        if r.status_code == 200:
            text = render_template('zoomIn')
            return question(text)
    except Exception as e:
        return question("Sorry, the map was busy, please try again!")

@ask.intent('zoomOutIntent')
def zoom_out():

    url = "https://globe-sb.herokuapp.com/alexaPosition"
    try:
        r = requests.post(url,data={"zoom_delta":3})
        if r.status_code == 200:
            text = render_template('zoomOut')
            return question(text)
    except Exception as e:
        return question("Sorry, the map was busy, please try again!")


@ask.intent('quitIntent')
def quit_map():

    return statement("Thank you for using globe, goodbye!")


### DATA PREFERENCE FUNCTIONS ###

@ask.intent('setDataIntent')
def send_data(data_pattern_num): # 1 - 4
    url = "https://globe-sb.herokuapp.com/setDataPattern"
    try:
        index = data_sets.index(data_pattern_num)
        r = requests.post(url,data={'pattern_id':index})
        if r.status_code == 200:
            return question("Alright, updating data pattern")
    except Exception as e:
        return question("Sorry, map was busy, please try again!")

@ask.intent('setMapIntent')
def update_map(map_num): # 1-3
    url = "https://globe-sb.herokuapp.com/setMapStyle"
    try:
        r = requests.post(url,data={'map_style':map_num})

        if r.status_code == 200:
            return question("Sounds good, updating map for you.")
    except Exception as e:
        return question("Sorry, couldn't find map, please try again.")


### CONFIG FUNCTIONS ###

@ask.intent('testAlexaIntent')
def hello_world():

    return statement("Hello World!")



if __name__ == '__main__':
    app.run(debug=True)
