import requests
import _json

response_API = requests.get('https://remoteok.com/api')
print(response_API.status_code)