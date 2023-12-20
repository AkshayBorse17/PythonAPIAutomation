from faker import Faker
from dotenv import load_dotenv
import os

faker=Faker()

def create_token_payload():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def create_token_payload2():
    load_dotenv()
    username=os.getenv("USER")
    password=os.getenv("PASSWORD")
    payload = {
        "username": username,
        "password": password
    }
    return payload



def create_booking_payload():
    payload = {
        "firstname": "Pat",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_booking_faker():
    json_payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            #         "checkin": str(faker.date_between(start_date='-3y', end_date='today')),
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "WiFi", "Extra Bed"))
    }
    return json_payload


def update_booking_payload():
    payload = {
        "firstname": "Kaju",
        "lastname": "Herapheri",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def par_update_booking_payload():
    payload = {
        "firstname": "Raju",
        "lastname": "Herapheri",
        "totalprice": 1110000000000008,
    }
    return payload
