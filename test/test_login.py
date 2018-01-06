import requests

# r = requests.post('http://127.0.0.1:5000/login', auth=('admin', 'default'))
# print(r.text)
#
# token = "YWRtaW46MC4wNDk4NjYxNjAwODEwMzY4NDoxNTE1MjU4NDM3LjE3NDQyNDI="
# r = requests.post('http://127.0.0.1:5000/test', params={'token': token})
# print(r.text)

r = requests.get('http://localhost:5000/client/login')
print(r.text)
print("===========")
print(r.history)
print("===========")
print(r.url)
print("===========")

uri_login = r.url.split('?')[0] + '?user=admin&pw=default'
r2 = requests.get(uri_login)
print(r2.text)
print(r2.headers)
print("===========")
print(r2.history)
r3 = requests.get("http://localhost:5000/test", params={'token':r2.text})
print(r3.text)