import requests

response = requests.get("https://api.open-notify.org/iss-pass.json", parameter=parameter)

print(response.json())