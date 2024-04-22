class Base:
    def __init__(self) -> None:
        print("Base initializer")

    def f(self):
        print("Base.f()")

class Sub(Base):
    def __init__(self):
        print("Sub initializer")
        super().__init__()
    
    def f(self): # override
        print("Sub.f()")

if __name__ == "__main__":
    s = Sub() 
    # python doesn't automatically call base class __init__ when subclass has its own



