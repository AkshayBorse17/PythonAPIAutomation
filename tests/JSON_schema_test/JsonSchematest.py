from jsonschema import validate
from jsonschema.exceptions import ValidationError
from src.constants.api_constants import *
from src.helpers.headers import *
from src.helpers.payload import *
import os


def read_schema(path):
    with open(path, 'r') as file:
        return json.load(file)


@pytest.mark.positive
def test_createbooking_tc2():
    res, data = post_req(url=baseURL(), auth=None, header=json_headers(), payload=payload_create_booking_faker())

    path=os.getcwd()+"/schema.json"
    schema=read_schema(path)
    try:
        validate(instance=data,schema=schema)
    except ValidationError as e:
        print(e.message)
    else:
        print("all good>>>")
