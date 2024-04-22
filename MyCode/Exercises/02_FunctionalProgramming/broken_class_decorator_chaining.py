# Chaining Class Decorators: BROKEN
# Each decorator works on its own, but can't chain them as defined
# Would Class Inheritance be more appropriate?
import functools
import time
class CallCount:
    
    
    def __init__(self,f):
        self.f = f
        self.count = 0
        
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        result = self.f(*args, **kwargs)
        
        return result
    

class LastCalled:
    def __init__(self,f):
        self.f = f
        self.last_call_time = None
        self.last_called_elapsed = None # num seconds since last call
        
    def __call__(self, *args, **kwargs):

        result = self.f(*args, **kwargs)
        
        now = time.time()
        if self.last_call_time is None:
            self.last_call_time = now
        
        self.last_called_elapsed = now - self.last_call_time
        self.last_call_time = now

        return result

@CallCount    
@LastCalled
def hello(name):
    print(f"Hello {name}!")

