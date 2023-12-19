import requests
import openpyxl
import pytest
from src.constants.api_constants import *
from src.helpers.headers import *

c=0
def make_request_auth(username, password):

    payload = {
        "username": username,
        "password": password
    }
    global c
    c=c+1

    response = requests.post(url=tokenURL(), headers=json_headers(), json=payload)
    return response,c


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials



def test_post_create_token():
    file_path = r"C:\Users\aksha\OneDrive\Desktop\PythonAPIAuto\tests\Data_Driven_Test\DataIP.xlsx"
    credentials = read_credentials_from_excel(file_path)

    print()
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response,c = make_request_auth(username, password)
        print(response)

        assert response.status_code == 200
    print(c)



