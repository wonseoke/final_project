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

request_url_dist = f"https://www.zipcodeapi.com/rest/fRJTo2YJmHwVfwLFleqpt2lDxb8vWVNZoDLNG8OOixB55eg1kuOI1zgSp4VNTUa5/distance.json/{zip_code_origin}/{zip_code_destination}/mile"

response = requests.get(request_url_dist)
parsed_response = json.loads(response.text) 

dist = parsed_response["distance"]

breakpoint()