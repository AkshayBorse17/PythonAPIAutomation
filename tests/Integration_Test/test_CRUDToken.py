from pprint import pprint
import pytest

from src.helpers.api_integration import *
from src.helpers.verify import *
from src.helpers.payload import *
from src.helpers.headers import *
from src.constants.api_constants import *
from src.helpers.headers import *



class Testbooking():

    ####Positive Test cases :
    # @pytest.fixture()
    @pytest.mark.positive
    def test_tokencreate_tc1(self):
        res,data=create_token(url=tokenURL(),auth=None,header=json_headers(),payload=create_token_payload())
        token=data["token"]
        statuscode(res.status_code, 200)
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        print(token)
        return token

    # @pytest.fixture()
    @pytest.mark.positive
    def test_createbooking_tc2(self):
        res,data=post_req(url=baseURL(),auth=None,header=json_headers(),payload=payload_create_booking_faker())
        statuscode(res.status_code,200)

        json_key_not_null(data["bookingid"])
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        id=res.json()["bookingid"]
        print()
        pprint(data)
        print(res)
        return id


    @pytest.mark.positive
    def test_readbooking_tc3(self, ):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)
        res, data = get_req(url=fullurl, auth=None, header=json_headers())

        statuscode(res.status_code, 200)
        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    @pytest.mark.positive
    def test_updatebooking_auth_tc4(self):
        id=Testbooking.test_createbooking_tc2(self)
        fullurl=baseURL()+str(id)
        auth=("admin","password123")

        # token = "token=" + Testbooking.test_tokencreate_tc1(self)
        headers = {
                "Content-Type": "application/json"

        }

        res,data=put_req(url=fullurl,auth=auth,header=headers,payload=update_booking_payload())

        statuscode(res.status_code,200)
        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)



    @pytest.mark.positive
    def test_updatebooking_token_tc5(self):
        id=Testbooking.test_createbooking_tc2(self)
        fullurl=baseURL()+str(id)

        token = "token=" + Testbooking.test_tokencreate_tc1(self)
        headers = {
                "Content-Type": "application/json",
                "Cookie": token

        }

        res,data=put_req(url=fullurl,auth=None,header=headers,payload=update_booking_payload())

        statuscode(res.status_code,200)
        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)


    @pytest.mark.positive
    def test_par_updatebooking_token_tc6(self):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)

        token = "token=" + Testbooking.test_tokencreate_tc1(self)
        headers = {
            "Content-Type": "application/json",
            "Cookie": token

        }
        res, data = patch_req(url=fullurl, auth=None, header=headers, payload=par_update_booking_payload())
        statuscode(res.status_code, 200)

        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    @pytest.mark.positive
    def test_deletebooking_token_tc7(self):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)

        token = "token=" + Testbooking.test_tokencreate_tc1(self)
        headers = {
            "Content-Type": "application/json",
            "Cookie": token

        }
        res, data = delete_req(url=fullurl, auth=None, header=headers)
        statuscode(res.status_code, 201)

        json_key_not_null(data)
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    ####Negative Test cases ::::::

    @pytest.mark.negative
    def test_tokencreate_tc8(self):
        res, data = create_token(url=tokenURL(), auth=None, header=json_headers(), payload=create_token_payload())
        token = data["token"]
        statuscode(res.status_code, 400)
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        print(token)
        return token

    # @pytest.fixture()
    @pytest.mark.negative
    def test_createbooking_tc9(self):
        res, data = post_req(url=baseURL(), auth=None, header=json_headers(), payload=create_booking_payload())
        statuscode(res.status_code, 400)

        json_key_not_null(data["bookingid"])
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        id = res.json()["bookingid"]
        print(data)
        print(res)
        return id


    @pytest.mark.negative
    def test_readbooking_tc10(self, ):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)
        res, data = get_req(url=fullurl, auth=None, header=json_headers())

        statuscode(res.status_code, 400)
        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    @pytest.mark.negative
    def test_update_kidding_tc11(self):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)
        auth = ("admin", "password123")

        # token = "token=" + Testbooking.test_tokencreate_tc1(self)
        headers = {
            "Content-Type": "application/json"

        }

        res, data = put_req(url=fullurl, auth=auth, header=headers, payload=update_booking_payload())

        statuscode(res.status_code, 400)
        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)


    @pytest.mark.negative
    def test_par_updatebooking_tc12(self):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)

        token = "token=" + Testbooking.test_tokencreate_tc1(self)
        headers = {
            "Content-Type": "application/json",
            "Cookie": token

        }
        res, data = patch_req(url=fullurl, auth=None, header=headers, payload=par_update_booking_payload())
        statuscode(res.status_code, 400)

        json_key_not_null(data)
        response_key_not_none(data["firstname"])
        response_time(res.elapsed.seconds)
        print(data)
        print(res)

    @pytest.mark.negative
    def test_deletebooking_tc13(self):
        id = Testbooking.test_createbooking_tc2(self)
        fullurl = baseURL() + str(id)

        token = "token=" + Testbooking.test_tokencreate_tc1(self)
        headers = {
            "Content-Type": "application/json",
            "Cookie": token

        }
        res, data = delete_req(url=fullurl, auth=None, header=headers)
        statuscode(res.status_code, 400)

        json_key_not_null(data)
        response_key_not_none(data)
        response_time(res.elapsed.seconds)
        print(data)
        print(res)






