import requests

# response = requests.post('http://120.79.144.50:8000/hm/app/login/', json={})
# print(response.content)

resp1 = requests.options('http://120.79.144.50:8000/hm/app/login/')
print(resp1.headers)
