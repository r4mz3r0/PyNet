import requests
response = requests.get('http://github.com')
try: 
    for key, value in response.headers.items(): 
        print('%s: %s' % (key, value))
except Exception as Error: 
    print('%s' % (error))
