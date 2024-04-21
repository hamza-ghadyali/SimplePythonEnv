Classes_OOP README

order:

shipping
static-method-inheritance-demo
class-method-inheritance-demo
template-method-inheritance-demo
multiple-inheritance
class-decorators
    autorepr-demo - checkpoints:
        location_040 - starting point
        location_090 - import at repl
        location_140 - import at repl
        location_300 - final result
    clip-04 Class Decorator Factories
        deep example that also uses function decorator factories
        and composes many lessons together
        WORTH RE-REVIEWING
        ./invariant-demo/itinerary_170.py - final result

        the function defined as "invariant" is the factory of class decorators
        easy to see since it returns a class decorator
        interestingly it modifies the class in such a way that every class method
        is decorated with a particular function decorator
        this in turn reduces code duplication

data-classes:
    clip-04/inv-demo/location_400.py:
        recommend using @dataclass(frozen=True) 
        # frozen enables immutability which should be preferred as best practice
        # frozen=true with eq=True allows hashing
        # hashing allows using dataclass instances in a set
        # __post_init__ for validating attribute arguments (inputs) upon construction


    type-annotated class attributes specify the data class members

    



see comments in files