# We'll update this starting from shipping_280.py
# We will explore encapsulation properties
# starting with @property for celsius
# we are transforming simple attributes into PROPERTIES
# this leads us to having a getter method
# and then we create a setter method


import iso6346

class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        # if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
        #     raise ValueError("Temperature too hot!")
        # self._celsius = celsius
        # the above three lines replaced by one line below avoids code duplication
        self.celsius = celsius # "self encapsulation"
        # seems a little magical though
        # but then again the actual value is stored in self._celsius

    @property # creates a property object with this being the getter method
    def celsius(self):
        return self._celsius
    
    @celsius.setter # modifies property object by including a setter method.
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value
        return
    

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )

# compare this to shipping_260.py
# everything that was broken is now fixed here