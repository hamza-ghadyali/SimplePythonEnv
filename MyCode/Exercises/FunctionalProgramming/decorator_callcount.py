import time
class CallCount:
    def __init__(self,f):
        self.f = f
        self.count = 0
        self.last_call_time = None
        self.last_called_elapsed = None # num seconds since last call
        
    def __call__(self, *args, **kwargs):
        self.count += 1
        result = self.f(*args, **kwargs)
        
        now = time.time()
        if self.last_call_time is None:
            self.last_call_time = now
        
        self.last_called_elapsed = now - self.last_call_time
        self.last_call_time = now

        return result


    
@CallCount    
def hello(name):
    print(f"Hello {name}!")

#hello = CallCount(hello)

if __name__ == "__main__":
    print(hello.count, hello.last_call_time, hello.last_called_elapsed)
    hello('Fred')
    print(hello.count, hello.last_call_time, hello.last_called_elapsed)
    
    time.sleep(2); hello('Ann')
    print(hello.count, hello.last_call_time, hello.last_called_elapsed)
    time.sleep(2.5); hello('Curtis')
    print(hello.count, hello.last_call_time, hello.last_called_elapsed)
    
    
