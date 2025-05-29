import requests as r
apikey = ""
with open('C:/Users/DELL/Desktop/api-keys/news.txt','r') as f:
   apikey= f.read()
url = f"https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey={apikey}"
res=r.get(url)
j=res.json()
for key in j['articles']:
    print(key['content']+'\n\n')
