import requests 
import json

API_KEY = "2369b101e6f002368134406dd2d008e3"
URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_city_temperature(city_name):
    complete_url = f"{URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(complete_url).json()
    current_temperature = response["main"]["temp"]
    return current_temperature

def get_city_pressure(city_name):
    complete_url = f"{URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(complete_url).json()
    current_pressure = response["main"]["pressure"]
    return current_pressure

def get_city_humidity(city_name):
    complete_url = f"{URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(complete_url).json()
    current_humidity = response["main"]["humidity"]
    return current_humidity

if __name__ == "__main__":
    current_tempreture = get_city_temperature("tunis")
    current_pressure = get_city_pressure("tunis")
    print(current_tempreture, current_pressure)








