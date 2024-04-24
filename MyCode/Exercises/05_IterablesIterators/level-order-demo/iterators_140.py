def _is_perfect_length(sequence):
    """True if sequence has length 2ⁿ - 1, otherwise False.
    """
    n = len(sequence)
    return ((n + 1) & n == 0) and (n != 0)

"""
uses bitwise operator &(and) on binary representation
1 = 1
3 = 11
7 = 111

return ((n+1) & n == 0)

examples:
n=1: 10 & 01  == 0 
n=3: 100 & 011 == 0
n=7: 1000 & 0111 == 0
"""


class LevelOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"Sequence of length {len(sequence)} does not represent "
                "a perfect binary tree with length 2ⁿ - 1"
            )
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._index]
        self._index += 1
        return result

    def __iter__(self):
        return self


if __name__ == "__main__":
    mydict = {i: _is_perfect_length(["x"]*i) for i in range(17) }
    print(mydict)

    notperfecttree = [*"+-abc"]
    iterator = LevelOrderIterator(notperfecttree) 
    # ValueError exception is raised as desired

    






