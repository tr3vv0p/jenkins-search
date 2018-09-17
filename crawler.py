from yandex_search import Yandex
import requests

ya = Yandex(api_user='porteriv', api_key='03.377714869:ed2a5967157a814867387f0b05e5d289')

class PageLimitException(Exception):
    pass

for i in range(10):
    try:
        re_xml = ya.search('$title:"Dashboard [Jenkins]" Credentials', page=1).items
    except PageLimitException:
        print('Page limit exceeded')
    final_list = []
    for item in re_xml:
        page = requests.get(item["url"]+"/configureSecurity/")
        contents = page.content
        label_tag = page.text[page.text.find('Anyone can do anything') - 127:page.text.find('Anyone can do anything')]
        if 'checked="true"' in label_tag:
            final_list.append(item)

# page = requests.get('http://185.143.172.133:8080/configureSecurity/')
# contents = page.content
# print('Anyone can do anything' in page.text)
#
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(contents, 'html.parser')
# soup.find_all('label', attrs={'checked': 'true'})