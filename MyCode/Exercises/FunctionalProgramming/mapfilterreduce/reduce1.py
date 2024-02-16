from functools import reduce
import operator

r = reduce(operator.add, [1,2,6,4,5])
print(r) # 18

# reduce in python is also known as accumulate, fold, aggregate in other langs

# define a function that prints each time to see progress of reduce()
def mul(x,y):
    print(f"mul {x=} {y=} ")
    return x*y

r = reduce(mul, range(1,10))

print(r)

