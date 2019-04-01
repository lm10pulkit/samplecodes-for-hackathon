import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'data':['ache'],})
print(r.json())