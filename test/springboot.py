import json
import requests

resp = requests.post('http://127.0.0.1:8080/api/sql/select', json={
                     'sql': 'select c.id, c.first_name, c.last_name from Customer c', 'params': []})
jsnRsp = json.loads(resp.content)
print(jsnRsp['message'])
