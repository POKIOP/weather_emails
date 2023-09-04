import requests 
import json

API_KEY = "2369b101e6f002368134406dd2d008e3"
URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_city_tempreture(city_name):
    complete_url = f"{URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(complete_url).json()
    current_temperature = response["main"]["temp"]
    return current_temperature

if __name__ == "__main__":
    current_tempreture = get_city_tempreture("warsaw")
    print(current_tempreture)








