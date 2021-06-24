#install (requests and playsound) library 

import time

import requests


from playsound import playsound

# Note Note Note
# This Programme Work only For South East Delhi Region  


day = input("Please Enter Date\n DD = Day \n")
Month = input("Please Enter Month\n MM = Month \n")
Dose = input("Please Enter Dose Number \n Dose = 1 or Dose = 2 \n")

URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=144&date=day{}-Month{}-2021'.format(day, Month)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def FreeCoxaxinFinder():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for I in data:
        if((I["min_age_limit"] == 18) & (I["fee_type"] == "Free") & (I["available_capacity_dose{}".format(Dose)] > 0 ) & (I["vaccine"] == "COVAXIN")):
            counter += 1
            print(I["name"])
            print(I["pincode"])
            print(I["available_capacity_dose1"])
            print(I["vaccine"])
            print(I["fee_type"])

            #PLease Change Sound Directory If you Use same Code
            
            #playsound('C:/Users/Shubham/Downloads/00sound.mp3')
            return True
    if(counter == 0):
        print("Zero availability")
        return False


while(FreeCoxaxinFinder() != True):
    time.sleep(3)
    FreeCoxaxinFinder()