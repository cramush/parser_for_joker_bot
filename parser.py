import requests
from bs4 import BeautifulSoup
from lxml import etree

URL = "https://www.anekdot.ru/tags/"
HEADERS = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36", "accept": "*/*"}


def get_html(url, params=None):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_content(html):
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all("div", class_="tags-cloud")

    tags = []
    for item in items:
        tags.append({

        })


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")


parse()



