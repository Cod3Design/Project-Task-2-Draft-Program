"""
-ask user for zip code or city
-use provided information to make api call to openweathermap.org
-display data in a readable format
-use comments within the application where appropriate
-use functions including a main function
-allow the user to run the program multiple times
-validate user input
-use try/except blocks"""

import requests
import os
from apikey import apiK

validZip = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def convertK(tempk):
    degreeF = (float(tempk) - 273.15) * 9 / 5 + 32
    return f"{degreeF:.1f}F"


def main():
    os.system('cls')
    zipCode = input("Enter your 5-digit Postal Code or 'end' to quit: ")
    if zipCode.lower() == "end":
        pass
    else:
        for char in zipCode:
            if char not in validZip or len(zipCode) > 5:
                print("Sorry it seems like your zipcode is invalid!")
                main()
            else:
                pass
        try:
            apiCall = requests.get(f"http://api.openweathermap.org/data/2.5/weather?zip={zipCode}&appid={apiK}")
            weatherData = apiCall.json()
            dataShort = weatherData['main']
            cityName = weatherData['name']
            #print(weatherData)    #uncomment to see raw data in console
            print('=' * len("Press Enter to search again!"))
            print(cityName)
            print('=' * len("Press Enter to search again!"))
            print(f"Current Temp:\t{convertK(dataShort['temp'])}")
            print(f"Feels Like:\t{convertK(dataShort['feels_like'])}")
            print(f"Low:\t\t{convertK(dataShort['temp_min'])}")
            print(f"High:\t\t{convertK(dataShort['temp_max'])}")
            input("Press Enter to search again!")
            main()
        except:
            print("Oops something went wrong!")
            input("Press Enter to try again...")
            main()


if __name__ == "__main__":
    main()