# example use of star-args, kwargs for argument forwarding

def trace(f, *args, **kwargs):
    print(f"{args=}")
    print(f"{kwargs=}")

    result = f(*args, **kwargs)
    print(f"{result=}")

    return result

if __name__ == "__main__":
    trace(int, "f3", base=16)
    