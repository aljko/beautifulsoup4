import requests
import re
from bs4 import BeautifulSoup

conf = [
            ['coe', 'https://www.coe-recruitment.com/', ['span', 'id', "labelTitleOfPost"]],
            ['parl', 'https://apply4ep.gestmax.eu/search/index/lang/fr_FR', ['h2', 'class', 'list-group-item-heading']],
            # ['IGBMC', 'https://www.igbmc.fr/igbmc/emplois' ,['h3', '', '']]
        ]

for site in conf:
    response = requests.get(site[1])
    print();
    print(site[0])
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all(site[2][0], {site[2][1]: re.compile(site[2][2])})
        for post in posts:
            print(post.get_text())

