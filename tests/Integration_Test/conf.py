from src.helpers.headers import *
from src.helpers.verify import *
from src.helpers.api_integration import *
from src.helpers.payload import *
from tests.Integration_Test.test_CRUDTokenFixture import *

import pytest
import requests
@pytest.fixture()
@pytest.mark.positive
def test_tokencreate_tc1():
    res, data = create_token(url=tokenURL(), auth=None, header=json_headers(), payload=create_token_payload())
    token = data["token"]
    statuscode(res.status_code, 200)
    response_key_not_none(data)
    response_time(res.elapsed.seconds)
    return token


@pytest.fixture()
@pytest.mark.positive
def test_createbooking_tc2():
    res, data = post_req(url=baseURL(), auth=None, header=json_headers(), payload=create_booking_payload())
    statuscode(res.status_code, 200)

    json_key_not_null(data["bookingid"])
    response_key_not_none(data)
    response_time(res.elapsed.seconds)
    id = res.json()["bookingid"]
    return id
    print(data)
    print(res)
