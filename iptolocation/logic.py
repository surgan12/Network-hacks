import urllib.request ,json

raw=""
def back(data,entry):  
 url = 'https://ipfind.co/?ip=' + data;	
 response = urllib.request.urlopen(url)
 data = json.loads(response.read())
 entry.insert(0,data['country'])
