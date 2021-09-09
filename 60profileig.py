from bs4 import BeautifulSoup
import requests

#URL = "ลิงค์ IG"
request = requests.get(URL)
s = BeautifulSoup(request.text, "html.parser")
meta = s.find("meta", property="og:description")
s = meta.attrs['content'].split(" ")
data = {}
data['Name'] = s[-2]
data['-'] = s[-1]
data['Followers'] = s[0]
data['Following'] = s[2]
data['Post'] = s[4]
print(data)
