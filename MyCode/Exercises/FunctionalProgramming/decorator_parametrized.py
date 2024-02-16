def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(f'Argument {index} must be nonnegative')
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value, size):
    return [value] * size


check_third = check_non_negative(2)
# this is essentially validator func with index=2

# check_non_negative can be viewed as a factory of decorators
# we previously discussed function-factories, this is a decorator-factory
# where for the index argument gets attached to an instance of validator

@check_third
def create_list2(value, size, junk):
    return [value] * size

if __name__ == "__main__":
    a = create_list('a', 3)
    print(a)

    #create_list(123, -6)

    create_list2(1,2,3)
    create_list2(1,2,-3)

