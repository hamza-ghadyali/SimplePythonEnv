class ShippingContainer:

    next_serial = 1337 # class attribute

    @staticmethod # essentially a good practice, better to use classmethod see v2shipping.py
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
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





    