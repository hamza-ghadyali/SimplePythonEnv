import time
# make_timer is an example of a "Factory Function"
# by returning different instances of elapsed function
def make_timer():
    last_called = None
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        
        result = now - last_called
        last_called = now
        return result
    return elapsed

t1 = make_timer()
t2 = make_timer()
t1()
t2()
# t1 and t2 are different independent instances of elapsed function
# and they both have a float object attached to them
# closures keep enclosing-scope objects alive
# in this case: last_called is kept alive as a float object
print(t1.__closure__)
print(t2.__closure__)
