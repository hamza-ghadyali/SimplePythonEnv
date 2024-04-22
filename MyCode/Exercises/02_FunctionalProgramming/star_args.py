def hv(*args):
    print(args)
    print(type(args)) # tuple

def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i) #initialize v with the first element of lengths tuple
    for length in i:
        v *= length # 1st iteration of loop gets tuple's 2nd element
    return v

def hypervolume2(*lengths):
    v = 1
    for length in lengths:
        v *= length
    return v

# throws a better error if called with no args
# e.g. `hypervolume()`
def hypervolume3(length, *lengths):
    v = length
    for length in lengths:
        v *= length
    return v


if __name__ == "__main__":
    print(hypervolume(3,4,5))
