import pytest

from src.helpers.api_integration import *
from src.helpers.verify import *
from src.helpers.payload import *
from src.helpers.headers import *
from src.constants.api_constants import *

class Testbooking():

    # @pytest.fixture()
    def test_token_tc1(self):
        res,data=create_token(url=tokenURL(),auth=None,header=json_headers(),payload=create_token_payload())

        statuscode(res.status_code,200)
        json_key_not_null(data)
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    # @pytest.fixture()
    def test_createbooking_tc2(self):
        res,data=post_req(url=baseURL(),auth=None,header=json_headers(),payload=create_booking_payload())
        statuscode(res.status_code,200)

        json_key_not_null(data["bookingid"])
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        id=res.json()["bookingid"]
        return id
        print(data)
        print(res)

    def test_readbooking_tc3(self,):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL()+str(id)
        res,data=get_req(url=fullurl,auth=None,header=json_headers())

        statuscode(res.status_code,200)
        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    def test_updatebooking_tc4(self):
        id=Testbooking.test_createbooking_tc2(self)
        fullurl=baseURL()+str(id)
        res,data=put_req(url=fullurl,auth=None,header=json_headers(),payload=update_booking_payload())

        statuscode(res.status_code,200)
        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    def test_par_updatebooking_tc5(self):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)
        res, data = patch_req(url=fullurl, auth=None, header=json_headers(), payload=par_update_booking_payload())
        statuscode(res.status_code, 200)

        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    def test_deletebooking_tc6(self):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)
        res, data = delete_req(url=fullurl, auth=None, header=json_headers())
        statuscode(res.status_code, 201)

        json_key_not_null(data)
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        print(data)
        print(res)





