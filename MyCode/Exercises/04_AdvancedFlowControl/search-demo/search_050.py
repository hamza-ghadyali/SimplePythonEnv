from bisect import bisect_left

s = [5, 8, 19, 34, 35, 53]


def contains(sequence, value):
    index = bisect_left(sequence, value)
    return sequence[index] == value


if __name__ == "__main__":
    print(contains(s,4))
    print(contains(s,5))
    print(contains(s,7))
    print(contains(s,18))
    print(contains(s,19))
    print(contains(s,20))
    print(contains(s,52))
    print(contains(s,53))
    print(contains(s,55))

# at the repl
# from search import *
# contains(s,70) # error, see search_060.py to fix

