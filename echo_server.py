#Author: Samuel Resendez


from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')


### TRAVEL FUNCTIONS ###
@ask.intent('goToDestinationIntent')
def travel_to_location(location):
    # location is name of location


    #do post request

    return "going to location" + str(location)


### DATA PREFERENCE FUNCTIONS ###




### CONFIG FUNCTIONS ###

@ask.intent('testAlexaIntent')
def hello_world():

    return statement("Hello World!")





if __name__ == '__main__':
    app.run(debug=True)
