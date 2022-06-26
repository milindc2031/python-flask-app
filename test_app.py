import requests

response = requests.get('http://127.0.0.1:3200/home')
response.raise_for_status()  # will raise exception when not a 2xx response
if response.status_code != 204:
    return response.json()
