import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
a = r.status_code
print(a)