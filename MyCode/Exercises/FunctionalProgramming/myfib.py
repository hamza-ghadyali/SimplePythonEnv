from functools import cache, lru_cache

# try using either cache or lru_cache, or neither, but not both...
# good example of builtin decorator, and builtin parametrized decorator

#@cache
@lru_cache(maxsize=3)
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    for i in range(400):
        print(i, fib(i))

