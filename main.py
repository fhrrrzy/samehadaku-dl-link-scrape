from bs4 import BeautifulSoup 
import requests
import json
from rich import print

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

links = {}

def make_req(url, header):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")

    dl = soup.find('div', {'class' : 'download-eps'})
    zippy = dl.find_all('ul')[0].find_all('li')[3].find_all('a', href=True)[0]["href"]

    return zippy

for ep in range(1,12):
    url = f"https://194.163.183.129/made-in-abyss-season-2-episode-{ep}/"
    x = make_req(url, header=headers)
    newep = {f"Episode-{ep}":x}
    links.update(newep)

print(links)