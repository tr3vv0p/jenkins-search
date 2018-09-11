from yandex_search import Yandex

ya = Yandex(api_user='tronder-alex', api_key='03.413734275:019bcc08783d4bdce16febc2f0252483')
re_xml = ya.search('public jenkins instance', page=1).items()
print(re_xml)