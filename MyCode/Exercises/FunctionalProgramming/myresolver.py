import socket
from typing import Any

""" 
defining Resolver object to be callable like a function 
using __call__ definition
this is also an example of creating a stateful function
in this case self._cache holds a state between calls

at the repl:
from myresolver import Resolver
resolve = Resolver() # we now have a callable instance: resolve
resolve('google.com')
resolve.has_host('google.com') # true
print(resolve._cache)
resolve.clear()
resolve.has_host('google.com') # false
""" 
class Resolver:
    def __init__(self) -> None:
        self._cache = {}

    def __call__(self, host, *args: Any, **kwds: Any) -> str:
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        
        return self._cache[host]
    
    def clear(self):
        self._cache.clear()

    def has_host(self,host):
        return host in self._cache
    

    

    

