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

def read_from_xl(filepath):
    credntials=[]
    workbook=openpyxl.load_workbook(filepath)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credntials.append({"username":username,"password":password})
    return credntials



filepath=r"C:\Users\aksha\OneDrive\Desktop\PythonAPIAuto\tests\Data_Driven_Test\DataIP.xlsx"
@pytest.mark.parametrize("cred",read_from_xl(filepath))
def test_token_req(cred):
    username=cred["username"]
    password=cred['password']
    res=make_request_auth(username,password)