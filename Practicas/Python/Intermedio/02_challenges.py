## Challenges ##

"""Print numbers from 1 to 100 with the following rules:
    - For multiples of 3, print "Fizz" instead of the number.
    - For multiples of 5, print "Buzz" instead of the number.
    - For multiples of both 3 and 5, print "FizzBuzz" instead of the number.
"""

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)

fizzbuzz()
