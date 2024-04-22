# Examples of map()

# built-in ord function returns the Unicode code point for a one-character string.

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
                result = f(*args, **kwargs)
            return result
        
        return wrap

m = map(ord, "The quick brown fox")
print(m) # map object is an iterator object, lazy evaluation

T = Trace()
result = map(T(ord), "The quick brown fox")
next(result)
next(result)

#print(list(result))

def combine(x,y):
    return f"{x}{y}"


notes1 = ['b','c','d','e','f','g','a','b']
notes2 = ['flat','natural','natural','flat','natural']
l = list(map(combine, notes1, notes2))
print(l)
# since notes2 is shorter, map ends there without raising exception

# maps and comprehensions
a = [str(i) for i in range(5)]
b = list(map(str, range(5)))
print(a)
print(b)


