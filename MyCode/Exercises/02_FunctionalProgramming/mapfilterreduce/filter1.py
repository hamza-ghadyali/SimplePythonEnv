# filter()

# filter(function_that_takes_one_argument, sequence)

# returns a iterable object of type filter
# lazy evaluation

notzeros = filter(None, [0,-1,1,1,-1,0,2])

print(list(notzeros))

positives = filter(lambda x: x>0, [-2,2,-4,4,0,2,0,3,-3])

print(list(positives))

positives = filter(lambda x: x > 0, range(-5,5))

print(list(positives))

