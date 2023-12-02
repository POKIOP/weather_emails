import requests 
import json
from string import Template

API_KEY = "2369b101e6f002368134406dd2d008e3"
HUMIDITY_MESSAGE = Template('humidity is: $humidity %.')
PRESSURE_MESSAGE = Template('pressure is: $pressure hPa')
TEMPERATURE_MESSAGE = Template('temperature is: $temperature C degrees')
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

def prepare_message(user):
    separated_fields = [field.strip() for field in user.weather_fields.split(",")]
    
    message_content = {"user_name": user.name, "temperature": TEMPERATURE_MESSAGE.substitute(temperature = get_city_temperature(user.city)), "pressure": PRESSURE_MESSAGE.substitute(pressure = get_city_pressure(user.city)), "humidity": HUMIDITY_MESSAGE.substitute(humidity = get_city_humidity(user.city))}
    message = [message_content.get(field) for field in separated_fields]
   
    if not message:
        return None
    
    return f"""Good morning {user.name} \n\nToday at {user.city} {", ".join(message)}"""

if __name__ == "__main__":
    current_tempreture = get_city_temperature("tunis")
    current_pressure = get_city_pressure("tunis")
    print(current_tempreture, current_pressure)








