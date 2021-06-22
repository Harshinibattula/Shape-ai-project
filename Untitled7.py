#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install requests


import requests
#import os
from datetime import datetime

api_key = '4cfe54a2e7bf735a604003f9b67496c7'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = (api_data["main"]["temp"]) - 273.15
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
with open('shapeaiproject.txt','w') as f:
    # writes the data to shapeaiproject text file in the current working directory 
    details=""
    details+="-------------------------------------------------------------\n"+"Weather Stats for - {}  || {}\n".format(location.upper(), date_time)+"-------------------------------------------------------------\n"+"\nCurrent temperature is: {:.2f} deg C".format(temp_city)+"\nCurrent weather desc  :"+weather_desc+"\nCurrent Humidity      :"+str(hmdt)+ "%"+"\nCurrent wind speed    :"+str(wind_spd) +"kmph"


    f.write(details)
