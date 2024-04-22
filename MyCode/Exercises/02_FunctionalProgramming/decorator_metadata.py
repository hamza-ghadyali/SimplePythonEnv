import functools

def noop(f):
    @functools.wraps(f) # comment out to see effect
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    """This is a Docstring"""
    print("Hello World")

