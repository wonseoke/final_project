# app/quote_app.py

import csv
import json
import os
from dotenv import load_dotenv
from datetime import datetime

import requests

load_dotenv() #> loads contents of the .env file into the script's environment

def to_usd(my_price):
     return f"${my_price:,.2f}" #> $12,000.71
     
#
# INFO INPUTS
#
api_key = os.environ.get("ZIP_KEY") 

zip_code_origin = input("Zip Code of Origin: ") #to accept USER INPUT of origin zipcode
zip_code_destination = input("Zip Cod of Destination: ") #to accept USER INPUT of destination zipcode

request_url_dist = f"https://www.zipcodeapi.com/rest/{api_key}/distance.json/{zip_code_origin}/{zip_code_destination}/mile"

response = requests.get(request_url_dist) 
parsed_response = json.loads(response.text)  ##parses into json form

dist = parsed_response["distance"]  ##outputs the distance between the origin and destination

fc_truck = 0  ## to note Fixed Cost of borrowing a truck
## 10' Truck	$20
## 15' Truck	$30
## 17' Truck	$30
## 20' Truck	$40
## 26' Truck	$40

worker = 0  ## to note number of workers
hours = 0   ## to note number of hours to be spent

size_move = input("s1, s2, s3, s4, s5: ") #to accept USER INPUT of the size of the move
## Studio to 1 Bedroom == s1
## 1 Bedroom to 2 Bedroom  == s2
## Home up to 2 bedrooms == s3
## 2 Bedroom Home to 3 Bedroom Apt == s4
## 3 Bedroom Home to 4 Bedroom Home == s5


if size_move == "s1":
    fc_truck = float(20)
    worker = float(2)
    hours = float(1)
elif size_move == "s2":
    fc_truck = float(30)
    worker = float(2)
    hours = float(2)
elif size_move == "s3":
    fc_truck = float(30)
    worker = float(2)
    hours = float(3)
elif size_move == "s4":
    fc_truck = float(40)
    worker = float(3)
    hours = float(3)
elif size_move == "s5":
    fc_truck = float(40)
    worker = float(4)
    hours = float(3)

tc_truck = (fc_truck + (dist*2.5)) ## dist * 2.5 is the variable cost per mile 
working_capital =  (65*worker*hours) ## $65 per hour per worker

bid = to_usd(tc_truck + working_capital)

print(bid)

