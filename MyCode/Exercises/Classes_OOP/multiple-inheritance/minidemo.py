class Base1:
    def __init__(self):
        print("Base1.__init__")

class Base2:
    def __init__(self):
        print("Base2.__init__")

class Sub(Base1, Base2):
    pass


s = Sub() # prints "Base1.__init__" only

# need super() to call both other __init__

