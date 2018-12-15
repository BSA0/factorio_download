import requests
from bs4 import BeautifulSoup

def getting_versions(url):
    r = requests.get(url)
    print(r.text)
    tree = BeautifulSoup(r.text, "lxml")
    p = tree.find('div', {'class': 'span4 index-sidebar'}).find('dl').find('dd')
    print(p)
