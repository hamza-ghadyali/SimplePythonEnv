def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def northerncity(s = "Tromsø"):
    print(s) # what will it print? why?
    return s

print(northerncity())
print(northerncity('˙©ƒƒ∂ß∂'))
