class ShippingContainer:

    next_serial = 1337 # class attribute

    # @staticmethod # essentially a good practice, better to use classmethod here
    
    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result
    
    # NAMED CONSTRUCTOR EXAMPLE:
    @classmethod
    def create_empty(cls, owner_code):
        result = cls(owner_code, contents=[]) # this will call __init__ to construct instance
        return result
    
    @classmethod
    def create_with_items(cls, owner_code, items):
        result = cls(owner_code, contents = list(items))
        return result
        
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code # instance attribute
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

        return
    
if __name__ == "__main__":
    c1 = ShippingContainer("YML", ['books'])
    c2 = ShippingContainer("MAE", ['tools'])
    print(c1.serial, c2.serial)
    print(ShippingContainer.next_serial)
    
    
# There is no class scope in python
# Python scopes: LEGB:  Local, Enclosing, Global, Builtin


# @staticmethod better when...
#     no access needed to either class or instance objects
#     most likely an implementation detail of the class (and name should start with "_")


    