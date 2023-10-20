from datetime import *
import requests
try:
    API_key="50754c41dff5e47031441f75815f7280"
    location=input("Enter the city:")


    url=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_key}"

    response=requests.get(url).json()['weather'][0]['main']
    temp=round(requests.get(url).json()['main']['temp'])


    print("The weather in the ",location,"is :",response)

    print("The weather in the ",location,"is :",temp)
except:
    print("An error detected... visit the website")