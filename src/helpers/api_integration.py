import json
import pytest
import requests as req



def create_token(url,auth,header,payload):
    res = req.post(url=url, auth=auth, headers=header, data=json.dumps(payload))
    data = res.json()
    return res,data

def post_req(url,auth,header,payload):
    res = req.post(url=url, auth=auth, headers=header, data=json.dumps(payload))
    data = res.json()
    return res,data


def get_req(url,auth,header):
    # id = str(post_req())
    # print(id)
    # fullurl = baseURL()+id
    res = req.get(url=url, auth=auth, headers=header)
    data = res.json()
    return res,data


def put_req(url,auth,header,payload):
    # id = str(post_req())
    # fullurl = baseURL()+id
    res = req.put(url=url, auth=auth, headers=header, data=json.dumps(payload))
    data = res.json()
    return res,data


def patch_req(url,auth,header,payload):
    # id = str(post_req())
    # fullurl = baseURL()+id
    res = req.patch(url=url, auth=auth, headers=header, data=json.dumps(payload))
    data = res.json()
    return res,data

def delete_req(url,auth,header):
    # id = str(post_req())
    # fullurl = baseURL()+id
    res = req.delete(url=url, auth=auth, headers=header)
    data = res.text
    return res, data



