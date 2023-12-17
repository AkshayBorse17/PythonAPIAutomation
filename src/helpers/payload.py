def create_token_payload():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def create_booking_payload():
    payload = {
        "firstname": "Rajuu",
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
