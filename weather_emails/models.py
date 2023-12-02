from dataclasses import dataclass


@dataclass
class User:
    name: str = ""
    city: str = ""
    weather_fields: str = ""
    email: str = ""