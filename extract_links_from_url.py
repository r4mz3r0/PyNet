from bs4 import BeautifulSoup 
import requests 

url = input("Enter a website to extract the URLs from: ") 

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebkit/537.36 (KHTML, like Gecko) chrome/39.0.2171.95 Safari/537.36'} 
response = requests.get("http://" + url, headers = headers) 
data = response.text
soup = BeautifulSoup(data, 'lxml') 

for link in soup.find_all('a'): 
    print(link.get('href')) 
