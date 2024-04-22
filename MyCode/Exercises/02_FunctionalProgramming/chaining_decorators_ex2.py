def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        result = x.encode('unicode-escape').decode('ascii')
        return result
    return wrap

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)
        
        return wrap

#Decorating Methods Example
class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix
    
    innertracer = Trace()

    @innertracer
    def make_island(self, name):
        return name + self.suffix    

if __name__ == "__main__":
    tracer = Trace()
    
    @tracer
    @escape_unicode
    def norwegian_island_maker(name):
        newname = name + 'øy'
        print(newname)
        return newname
    
    result = norwegian_island_maker('Llama') # set breakpoint here see order of execution
    print(result)

    result = norwegian_island_maker('Python')
    print(result)

    tracer.enabled = False
    result = norwegian_island_maker('Troll')
    print(result)

    #example 2: decorating methods
    im = IslandMaker('Island')
    result = im.make_island('Treasure')
    print(result)


    