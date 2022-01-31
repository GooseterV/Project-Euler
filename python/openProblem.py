import webbrowser
import os
from numpy import True_
import requests
import bs4 as BeautifulSoup
def downloadMinimal():
	for i in range(1, 773):
		res = requests.get(f"https://projecteuler.net/minimal={i}")
		with open(f"html/p{str(i).zfill(3)}-MINIMAL.html", "w", encoding="utf-8") as pfile:
			soup = BeautifulSoup(res.text, "html.parser")
			pfile.write(soup.prettify()) 
	DOWNLOADED = True_

def downloadAll():
	for i in range(1, 773):
		res = requests.get(f"https://projecteuler.net/problem={i}")
		with open(f"html/p{str(i).zfill(3)}.html", "w", encoding="utf-8") as pfile:
			soup = BeautifulSoup(res.text, "html.parser")
			pfile.write(soup.prettify()) 
	DOWNLOADED = True_

minimal = True
DOWNLOADED = False
if not DOWNLOADED:
	if minimal:
		downloadMinimal()
	elif not minimal:
		downloadAll()
if minimal:
	fp = f'html/p{input("Problem Number? ").zfill(3)}-MINIMAL.html'
else:
	fp = f'html/p{input("Problem Number? ").zfill(3)}.html'
if not os.path.exists(fp):
	print("File is missing: " + fp)
else:
	webbrowser.open(os.path.abspath(fp))
