import requests

response = requests.get('http://0.0.0.0:8060/home')
response.raise_for_status()  # will raise exception when not a 2xx response
if response.status_code != 204:
    print("Response code=",response.status_code)
