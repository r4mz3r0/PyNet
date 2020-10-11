import requests
from requests.auth import HTTPBasicAuth
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('r4mz3r0', 'SECRETPASS')) 
response = requests.get('https://api.github.com/user', auth=('r4mz3r0', 'SECRETPASS')) 
print('Response.status_code: ' + str(response.status_code)) 
if(response.status_code == 0): 
    print('Login successful: ' + response.text) 

