from urllib.request import urlopen
from http.client import HTTPResponse
from threading import Thread


class ProxyScanIO:
    API = "https://www.proxyscan.io/api/proxy?format=txt&"

    @staticmethod
    def is_digit(obj=None) -> bool:
        return (isinstance(obj, int) or isinstance(obj, float))

    def __init__(self, API: str = API) -> None:
        if API != self.API:
            self.API = API

    def get_Proxies(self, count: int = 20, **kwargs) -> tuple:
        """
Parameter	Value	        Description

Level	    transparent,    
            anonymous,      
            elite           

Type	    http, https,
            socks4, socks5	Proxy Protocol

Last_Check	Any Number	    Seconds the proxy was last checked
Port	    Any Number	    Proxies with a specific port
Ping	    Any Number	    How fast you get a response after
                            you've sent out a request
Limit	    1 - 20	        How many proxies to list.
Uptime	    1 - 100	        How reliably a proxy has been running
Country	    2 Any Letters   Country of the proxy
Not_Country	2 Any Letters   Avoid proxy countries
"""

        if self.is_digit(count):
            self._limit = (count if isinstance(count, int)
                           else int(count))
        else:
            self._limit = 20
        self._end_link = self.API

        for i in kwargs.copy():
            value = kwargs[i]
            del kwargs[i]
            kwargs[i.lower()] = value

        for param in kwargs:
            value = kwargs[param]
            self._end_link += f"{param}={value}&"
        self._end_link = self._end_link[:-1]

        self._make_requests()

        return self._result

    def _add_result(self, limit: int) -> None:
        proxies = tuple()
        while len(proxies) < limit:
            try:
                url = f"{self._end_link}&limit={limit}"
                resp: HTTPResponse = urlopen(url)
                proxies += tuple(resp.read().decode("UTF-8")
                                 .splitlines())
                self._result += proxies
            except:
                pass

    def _make_requests(self) -> None:
        integer: tuple = (1,)*(self._limit//20)
        non_int = self._limit % 20 / 20,
        self._result = tuple()
        threads = tuple()
        for i in integer+non_int:
            t = Thread(target=self._add_result, args=(int(i*20),))
            t.start()
            threads += t,

        for t in threads:
            t.join()


pp = ProxyScanIO()
proxies = pp.get_Proxies()
print(proxies)
