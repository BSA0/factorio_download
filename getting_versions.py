import requests
from bs4 import BeautifulSoup


def getting_versions(url, selector):
    r = requests.get(url)
    p = BeautifulSoup(r.text, 'lxml')  # It returns BS tree
    # selector is described in settings.json and it's css selector(chrome -> copy selector)
    # p.select(selector) returns latest experimental release value in site factorio.com how ['<dd>value</dd>']
    # [0] just takes '<dd>value</dd>'
    # [4:-5] is deleting first and last 4 symbols
    return str(p.select(selector)[0])[4:-5]
