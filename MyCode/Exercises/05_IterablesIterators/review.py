# Example 1:
print("\nExample 1:")

iterator = iter([3.4,4,6,8.9])
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator = iter([3.4,4,6,8.9])

for item in iterator:
    print(item)





# Example 2:
print("\nExample 2:")

def iterable_oceans():
    yield "Arctic"
    yield "Pacific"
    yield "Atlantic"
    yield "Indian"

gen = iterable_oceans() # generator object

while gen:
    try:
        print(next(gen))
    except StopIteration:
        print("Reached end of generator")
        break



# StopIteration exception will get raised at the end
    
# Example 3:
print("\nExample 3:")

gen_squares = (x*x for x in range(int(1e100))) 
# despite large range, won't hang because generator

for i in range(5):
    print(next(gen_squares))

print("good and continue")

for i in range(5):
    print(next(gen_squares))

