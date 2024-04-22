# Class-bound Super Proxies
# how super() works, boils down to MRO, (and C3 algorithm)

class Animal:
    @classmethod
    def description(cls):
        return "An animal"


class Bird(Animal):
    @classmethod
    def description(cls):
        s = super()
        print(s)
        print(s.description)
        return s.description() + " with wings"


class Flamingo(Bird):
    @classmethod
    def description(cls):
        return super().description() + " and fabulous pink feathers"

if __name__ == "__main__":
    print(Animal.description())
    print(Bird.description())
    print(Flamingo.description())