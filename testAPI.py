import requests
import json

API_KEY = "or59R5MC.NLD3e4QtqcFpafuv4n2nV4GnyqjEeHDE"

URL = "https://payload.vextapp.com/hook/2Y5FMML2K0/catch/hello"
headers = {"Content-Type": "application/json", "Apikey": f"Api-Key {API_KEY}"}
data = {
    "payload": "tell me about the flood in pundranagara"
}

response = requests.post(URL, headers= headers, json=data)

print(response.text)