g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    print(inner)
    print(id(inner))
    print(id(l))
    inner()



