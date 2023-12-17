import requests
import json

# Make the GET request to the horoscope API
response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()  # Convert the response to JSON

# # Store the JSON data in a file
# # with open("horoscope_data.json", "w") as file:
# #     json.dump(data, file)
# #
# # print("Data stored successfully!")
#
# file=json.dumps(data)
# print(file)