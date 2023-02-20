from requests import Request
import requests
from requests import Response


"""
api documentation: https://avwx.docs.apiary.io/#introduction/airport-codes
"""

headers = {
  'Content-Type': 'text/plain',
  'Authorization': 'Token my_secret_api_token'
}

request = requests.get(url='https://avwx.rest/api/airsigmet', headers=headers)


response_body = request.json()


print(response_body)
