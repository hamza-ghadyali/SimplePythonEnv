class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude
    
    # target audience: developers
    def __repr__(self) -> str:
        return f"{type(self).__name__}(latitude={self.latitude}, longitude={self.longitude})"
    
    
    # observation: even with just __repr__ defined, without __str__ and __format__
    # str and format also show the same new display as repr
    # turns out that str delegates to repr, and format delegates to str, when not defined

    # target audience: humans (system consumers), human-readable, human-friendly
    def __str__v1(self):
        if self.latitude >= 0:
            lat = f"{self.latitude}° N"
        else:
            lat = f"{-1*self.latitude}° S"

        if self.longitude >= 0:
            lon = f"{self.longitude}° E"
        else:
            lon = f"{-1*self.longitude}° W"

        
        return ", ".join([lat, lon])
    
    def __str__(self) -> str: # v2
        result = (
        f"{abs(self.latitude)}° {'S' if self.latitude < 0 else 'N'}, "
        f"{abs(self.longitude)}° {'W' if self.longitude < 0 else 'E'}"
        )
        return result
    # this syntax allowed us to split source code across multiple lines

    def __str__v3(self) -> str: # v3: delegate to format, avoid code duplication
        return format(self)

    # this is used in format strings like f-strings: f"{oslo}"
    def __format__(self, __format_spec: str) -> str:
        component_format_spec = ".2f"
        
        prefix, dot, suffix = __format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"

        
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)


        return (
            f"{latitude}° {'S' if self.latitude < 0 else 'N'}, "
            f"{longitude}° {'W' if self.longitude < 0 else 'E'}")



# conventions for good __repr__ results:
    # include necessary state but be prepared to compromise
    # format as constructor invocation source code:
        # which allows the following:
        # oslo = Position(60.0, 10.7)
        # r = repr(oslo)
        # s = eval(r) # s is a new Position object created from string r
    
class EarthPosition(Position):
    pass

class MarsPosition(Position):
    pass

if __name__ == "__main__":
    oslo = Position(60.0, 10.7)
    print(f"{oslo=}")

    mauna_kea = EarthPosition(19.82, -155.47)
    olympus_mons = MarsPosition(-18.65, +133.8)

    print(mauna_kea) # uses str
    print(olympus_mons)

    print("oslo")
    print(repr(oslo))
    print(str(oslo))
    print(format(oslo))
    print(f"{oslo}")

    # # floating-point format spec
    # q = 7.748091e-5
    # print(format(q))
    # print(format(q, "f")) # fixed point representation
    # print(format(q, ".7f")) # 7 places post decimal
    # print(format(q, ".11f")) # 11 places post decimal
    # print(format(q, "+.11f")) # positive sign
    # print(format(q, ">+20.11f")) # right-align with field-width of 20
    # # float__format__ is what's actually being called here since q is float
    # print(type(q))
    # print(f"{q:>+15.11f}")
    # print(f"{q:>+15.5e}")


    matterhorn = EarthPosition(45.9763, 7.6586)
    print(format(matterhorn, ".1"))
    print(format(matterhorn, ".0"))
    print(format(matterhorn))
    print(f"The Matterhorn is at {matterhorn:.3}")
    print(f"{matterhorn=}") # uses repr



