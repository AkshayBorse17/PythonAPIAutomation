from dotenv import load_dotenv
import os

def test_auth():
    load_dotenv()
    username = os.getenv("USER")
    password = os.getenv("PASSWORD")
    token=os.getenv("TOKEN")
    print(os.getcwd())
    print(username,password,token)