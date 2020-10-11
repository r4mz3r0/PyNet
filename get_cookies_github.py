import requests
url = 'http://www.github.com'
response = request.get(url) 

for cookie in response.cookies: 
    print('Name:', cookie.name)
    print('Value:', cookie.value) 
    cookies.append(cookie.value) 
    if(not cookie.secure): 
        cookie.secure = '\x1b[31False\x1b[39;49m' 
    print('HTTPOnly:', check_httponly(cookie), '\n') 

print(set(cookies))
