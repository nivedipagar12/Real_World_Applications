'''
Project 3 : Geolocation using pandas and geocoders
            A program that takes an address from a csv file, converts it to longitude and latitude and stores them in the csv file
            Features :
                    The program concatenates the address, city, state and country columns to make a single string
                    Passes the string to the geocoder for conversion
                    Creates new columns for latitude and longitude and stores them
Created on: 28/01/2020
Created by: Nivedita Pagar
'''

import pandas as pd
from geopy.geocoders import ArcGIS

nom = ArcGIS() # Create an ArcGIS() object

data = pd.read_csv("supermarkets.csv") # get data from the CSV file

# Concatenate the street, city, state and country to create a single string of address for each row
data["Full Address"] = data["Address"] + ", " + data["City"] + ", " + data["State"] + ", " + data["Country"]

# Convert all the addresses to longitude and latitude using geocode() and apply() methods
data["Coordinates"] = data["Full Address"].apply(nom.geocode)

# Create new columns for storing the latitudes and longitudes
data["Latitude"] = data["Coordinates"].apply(lambda x : x.latitude)
data["Longitude"] = data["Coordinates"].apply(lambda x : x.longitude)
print(data) # Optional print statement to see the result
