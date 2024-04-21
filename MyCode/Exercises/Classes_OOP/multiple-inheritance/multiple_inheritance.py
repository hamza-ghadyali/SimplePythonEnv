class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort() # Why not super().sort() considering sort hasn't been overriden? 
        # Maybe because SortedList should likely have its own sort method later 
        # which should be preferred before necessarily going to the super() implementation.

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        #super().__init__(items)
        s = super()
        print(s)
        print(type(s))
        s.__init__(items)
        print(s.__init__)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("IntList only supports integer values")
        
    def add(self, item):
        self._validate(item)
        super().add(item)

class SortedIntList(IntList, SortedList):
    pass



if __name__ == "__main__":
    sil = SortedIntList([46,78,12]) # set a breakpoint here and step-into
    # when there is no __init__ in SortedList
    # only the first base-class __init__ is automatically called
    # but here IntList.__init__ calls super().__init__ which 
    # actually goes to SortedList.__init__ before going up to SimpleList.__init__

    sil.add(23) # set a breakpoint here and step-into
    # step-into results:
    # first goes to IntList.add, then from super().add goes on 
    # to SortedList.add, then SimpleList.add, 
    # then returns to super().add in Intlist before finishing up.
    
    mro = SortedIntList.__mro__
    print(mro)
    print(type(mro))
    
    #sil.add(5.7)

    # WARNING: Using arguments with super can be tricky!
    s = SortedIntList([])
    super(IntList, s).add("Not an integer bypassing Intlist.add validation!")
    print(s)
    

