import requests
from bs4 import BeautifulSoup
url = 'https://lichess.org/dafunkeymonkey'
r = requests.get(url)
soup = BeautifulSoup(r.text, features = 'html.parser')
titles = []
for h2 in soup.find_all("DaFunkeyMonkey"):
  titles.append(h2)
print(titles)

#My lichess username is @NicholasWB
