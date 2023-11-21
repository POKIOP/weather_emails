import requests 
import json
from string import Template

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

def prepare_message(fields, city_name):
    separated_fields = [field.strip() for field in fields.split(",")]
    temperature_message = Template('temperature is: $temperature C degrees')
    pressure_message = Template('pressure is: $pressure hPa')
    humidity_message = Template('humidity is: $humidity %.')
    message_content = {"temperature": temperature_message.substitute(temperature = get_city_temperature(city_name)), "pressure": pressure_message.substitute(pressure = get_city_pressure(city_name)), "humidity": humidity_message.substitute(humidity = get_city_humidity(city_name))}
    
    message = [] #3 linijki ponizej zmienic na jedna tak jak separated_fields
    for field in separated_fields:
        message.append(message_content.get(field))
    if not message:
        return None
    
    return "Hello " + ", ".join(message)

if __name__ == "__main__":
    current_tempreture = get_city_temperature("tunis")
    current_pressure = get_city_pressure("tunis")
    print(current_tempreture, current_pressure)








