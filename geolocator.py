

import csv
from geopy.geocoders import GoogleV3


geolocator = GoogleV3(api_key="AIzaSyC0q7QFF35WNbYWvr4hdFrlsr6RUCGYLRw")




location = geolocator.geocode("London")

print(location.address)
print(location.latitude, end= " ")
print(location.longitude)


