import requests
from bs4 import BeautifulSoup
for i in range(342, 773):
	res = requests.get(f"https://projecteuler.net/minimal={i}")
	with open(f"html/p{str(i).zfill(3)}.html", "w", encoding="utf-8") as pfile:
		soup = BeautifulSoup(res.text, "html.parser")
		pfile.write(soup.prettify()) 