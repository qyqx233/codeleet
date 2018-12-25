import requests

resp = requests.post('http://127.0.0.1:9000', json={'a': 100})
print(resp.content)