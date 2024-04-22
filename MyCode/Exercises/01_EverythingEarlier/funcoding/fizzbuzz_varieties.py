# elementary fizzbuzz

def fizzbuzz1(n):
    output = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    
    return output


def fizzbuzz2(n):
# this time avoid code duplication and avoid recomputation of modulo calculations
    output = []
    for i in range(1, n+1):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if out == "":
            out = str(i)
        output.append(out)

    return output


def fizzbuzz(n):
# this time avoid modulo calculations
    output = []
    mod3_counter = 0
    mod5_counter = 0
    
    def reset(counterstring):
        nonlocal mod3_counter
        nonlocal mod5_counter
        if counterstring == "mod3_counter":
            mod3_counter = 0
        elif counterstring == "mod5_counter":
            mod5_counter = 0
        else:
            raise ValueError
    
    for i in range(1, n+1):
        out = ""
        mod3_counter += 1
        mod5_counter += 1
        if mod3_counter == 3:
            out += "Fizz"
            #mod3_counter = 0      # Which is more readable? This?
            reset("mod3_counter")  # Or this?
        if mod5_counter == 5:
            out += "Buzz"
            #mod5_counter = 0
            reset("mod5_counter")
        if out == "":
            out = str(i)

        output.append(out)

    return output


if __name__ == "__main__":
    n = 15
    output = fizzbuzz(n)
    print(output)