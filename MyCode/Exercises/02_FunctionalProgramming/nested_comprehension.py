# nested comprehension

values1 = [x / (x-y) for x in range(10) if x > 5 for y in range(10) if x-y != 0]

values2 = [x / (x-y) 
          for x in range(10) 
          if x > 5 
          for y in range(10) 
          if x-y != 0]

values3 = []
for x in range(10):
    if x > 5:
        for y in range(10):
            if x - y != 0:
                values3.append(x/(x-y))

#  all equivalent: which is more readable?

vals = [[y*3 for y in range(x)] for x in range(5)]
print(vals)






