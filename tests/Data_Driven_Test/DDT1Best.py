import requests
import openpyxl
import pytest
from src.constants.api_constants import *
from src.helpers.headers import *

def make_request_auth(username, password):

    payload = {
        "username": username,
        "password": password
    }
    print(username,password)

    response = requests.post(url=tokenURL(), headers=json_headers(), json=payload)
    return response


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


file_path=r"C:\Users\aksha\OneDrive\Desktop\PythonAPIAuto\tests\Data_Driven_Test\DataIP.xlsx"

@pytest.mark.parametrize("user_cred", read_credentials_from_excel(file_path))
def test_post_create_token(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    response = make_request_auth(username, password)
    assert response.status_code == 200



