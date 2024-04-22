from bisect import bisect_left

s = [5, 8, 19, 34, 35, 53]


def contains(sequence, value):
    index = bisect_left(sequence, value)
    return (index != len(sequence)) and (sequence[index] == value)

# index is 0,1,2,3,4,5:
    # True and b --> return b
# index is 6: which in this case is len(s) == 6:
    # False and b --> return False (without executing b)





