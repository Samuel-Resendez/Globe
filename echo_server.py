#Author: Samuel Resendez


from flask import Flask, render_template
from flask_ask import Ask, statement, question
from geopy.geocoders import GoogleV3

""" Setting Global Vars """
app = Flask(__name__)
ask = Ask(app, '/')
geo_locator = GoogleV3(api_key="AIzaSyC0q7QFF35WNbYWvr4hdFrlsr6RUCGYLRw")

@ask.launch
def new_connection():
    """Called upon initialization"""
    return question("Hello, welcome to Globe, what would you like to see today?")



### TRAVEL FUNCTIONS ###

@ask.intent('goToDestinationIntent')
def travel_to_location(location):
    # location is name of location

    print(location)

    loc_obj = geo_locator.geocode(location)

    print(loc_obj.latitude, end=', ')
    print(loc_obj.longitude)

    #do post request

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




### CONFIG FUNCTIONS ###

@ask.intent('testAlexaIntent')
def hello_world():

    return statement("Hello World!")





if __name__ == '__main__':
    app.run(debug=True)
