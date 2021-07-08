import requests
import lxml.html
from bs4 import BeautifulSoup
import time

URL = "https://www.anekdot.ru/tags/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "*/*"}


def main():
    # t = time.time()
    request = requests.get(URL, headers=HEADERS)
    get_tag_list(request)
    # print(time.time() - t)


def get_tag_list(html):
    tree = lxml.html.document_fromstring(html.text)
    content = tree.xpath('//div[@class="tags-cloud"]/a')
    # print(content)
    tag_list = []
    for element in content:
        href = element.get("href")
        link = href.replace("/tags/", "")
        url = URL + link
        tag_list.append(url)
    # print(tag_list)
    for tag in tag_list:
        move_to_last_pages(tag)


def move_to_last_pages(url):
    request = requests.get(url, headers=HEADERS)
    tree = lxml.html.document_fromstring(request.text)
    pages = tree.xpath('//div[@class="pageslist"]/a')
    last_pages = tree.xpath('//div[@class="pageslist"]/a/text()')

    get_jokes_and_tags(url)
    list_links = []
    if "след. →" in last_pages:
        for element in pages:
            link = element.get("href")
            link = URL + (link.replace("/tags/", ""))
            list_links.append(link)
        second_joke = list_links[-1]
        move_to_last_pages(second_joke)


def get_jokes_and_tags(url):
    request = requests.get(url, headers=HEADERS)
    tree = lxml.html.document_fromstring(request.text)
    tag = tree.xpath('//div[@class="topicbox"]/h1/text()')

    soup = BeautifulSoup(request.text, "lxml")
    joke_list = soup.find_all("div", class_="text")

    joke_list_copy = joke_list.copy()

    for element in joke_list_copy:
        if 'www' in str(element):
            joke_list.remove(element)
            print("================================================================================================")
            print("removed")
    # print(joke_list)

    new_joke_list = []
    for element in joke_list:
        new_joke = str(element).replace('<div class="text">', "").replace('<br/>', "\n").replace('</div>', "")
        new_joke_list.append(new_joke)
    # print(new_joke_list)

    for element in new_joke_list:
        print("===============================================================================================")
        print(tag)
        print(element)


def filling_data():
    pass


if __name__ == '__main__':
    main()
