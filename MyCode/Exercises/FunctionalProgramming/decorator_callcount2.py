#explainer, live coding order for storytelling
#1,2,3,4...

class CallCount: #2
    def __init__(self, f):
        # bind f to instance
        self.f = f
        self.count = 0 #3
    
    #4
    def __call__ (self, *args, **kwargs):
        result = self.f(*args, **kwargs)
        self.count += 1
        return result
    
#1: start here in the story
def hello(name):
    print(f"Hello {name}!")

#2
#hello = CallCount(hello) # equiv to @CallCount decorator above def hello
#3
#hello.count

#4
# hello is an instance of CallCount object and needs to be callable
