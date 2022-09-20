import math

for i in range (1,101):
    if(i % 3 == 0 and i % 5 == 0):
        print("FiizBuzz")
    if(i % 3 == 0):
        print("Fizz")
    if(i % 5 == 0):
        print("Buzz")
    else:
        print(i)