from tests.Integration_Test.test_CRUDToken import *

def json_headers():

    headers={
        "Content-Type" : "application/json",
        "Authorization" : "Basic YWRtaW46cGFzc3dvcmQxMjM="

    }
    return headers

# def json_headers2():
#     token="token="+Testbooking.test_tokencreate_tc1()
#     headers={
#         "Content-Type" : "application/json",
#         "Cookie" : token
#
#     }
#     return headers

def xml_headers():
    headers={
        "Content-Type" : "application/xml"
    }
    return headers
