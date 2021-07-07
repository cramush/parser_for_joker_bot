import requests
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup

URL = "https://www.anekdot.ru/tags/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "*/*"}


def main():
    request = requests.get(URL, headers=HEADERS)
    get_tags(request)


def get_tags(html):
    tree = lxml.html.document_fromstring(html.text)
    content = tree.xpath('//div[@class="tags-cloud"]/a')
    # print(content)
    tags = []
    for element in content:
        href = element.get("href")
        tags.append(href)
    # print(tags)
    get_tags_html(tags)


def get_tags_html(tags):

    link = tags[0]
    link = link.replace("/tags/", "")
    url = URL + link
    # print(url)
    request = requests.get(url, headers=HEADERS)
    get_pages_count(request)


def get_pages_count(html):
    tree = lxml.html.document_fromstring(html.text)
    pages = tree.xpath('//div[@class="pageslist"]/a')
    next_pages = tree.xpath('//div[@class="pageslist"]/a/text()')
    # print(next_pages)

    list_links = []
    for element in pages:
        links = element.get("href")
        list_links.append(links)
    # print(list_links)

    count = 2
    if "след. →" in next_pages:
        link = list_links[0]
        link = link.replace("/tags/", "")[:-1] + str(count)
        url = URL + link
        print(url)
        request = requests.get(url, headers=HEADERS)
        get_jokes_and_tags(request)
    else:
        print(False)


def get_jokes_and_tags(html):
    tree = lxml.html.document_fromstring(html.text)
    tag = tree.xpath('//div[@class="topicbox"]/h1/text()')
    print(tag)
    soup = BeautifulSoup(html.text, "lxml")
    joke_list = soup.find_all("div", class_="text")
    joke_list_copy = joke_list.copy()

    for element in joke_list_copy:
        if '<img alt="Карикатура' in str(element):
            joke_list.remove(element)
    # print(joke_list)

    new_joke_list = []
    for element in joke_list:
        new_joke = str(element).replace('<div class="text">', "").replace('<br/>', "\n").replace('</div>', "")
        new_joke_list.append(new_joke)

    # print(new_joke_list)
    for element in new_joke_list:
        print("======================================================================================================")
        print(element)


def filling_data():
    pass


if __name__ == '__main__':
    main()
