import requests
from datetime import datetime
import json

api_key = "55c03ccfeca6b7edde879d44754b6d36"
location=input("Enter the location : ")
link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

data = requests.get(link).json()       # retrieve data and converting to json


temp = data['main']['temp'] - 273
desc = data['weather'][0]['description']
humidity = data['main']['humidity']
windsp = data['wind']['speed']
mintemp = data['main']['temp_min'] - 273
maxtemp = data['main']['temp_max'] - 273

dt = datetime.now().strftime("%d - %B - %Y  ||  %I : %M  %p")
print("\n\n")
print(f"Weather of {location.upper()}  |  Time : {dt}")
print("--------------------------------------------------")
print("Current Temperature  :     {:.2f}".format(temp))
print("Minimum Temperature  :     {:.2f}".format(mintemp))
print("Maximum Temperature  :     {:.2f}".format(maxtemp))
print("Weather Description  :   ",desc)
print("Current Humidity     :   ",humidity,"%")
print("Current Wind Speed   :   ",windsp,"m/s")

weatherdict = {"Location": location,"Temperature":{"temp":f"{temp:.2f}","mintemp":f"{mintemp:.2f}","maxtemp":f"{maxtemp:.2f}"},"Description":desc,"Humidity":humidity,"windspeed":windsp}

f = open("weatherhis.txt","a")
f.write(json.dumps(weatherdict))
f.write("\n")
f.close()