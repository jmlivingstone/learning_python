def outer() :
    "" ... """
    n = 1

    def inner() :
        """ ... """
        nonlocal n # also changes the variable gloally
        n =  2
        print(n)

    inner()
    print(n)

outer()
# 2
# creates a function that squares any value

def raise_val(n) :
    "" return the inner function """
    def innner(x) :
        "" raise x to the power of n """
        raised = x ** n
        return raised
    return inner

square = raise_val(2)
cube = raise_val(4)
print(square(2) , cube(4))

# LEGB rule
# Local scope
# Enclosing functions
# Global
# Built-in

# default arguments
def power(number, pow = 1) :
    new_value = number ** pow
    return new_value

power(9, 2)
# 81
power(9)
# 9

# flexible arguments
def add_all(*args) :
    """ Sum all values in args together """
    sum_all = 0

    for num in args:
        sum_all += num
    return sum_all

# **kwargs
def print_all(**kwargs):
    "print out key=value pairs in **kwrargs"""
    for key, value in kwargs.items():
        print(key + ":" + value)

print_all(name = "Hugo", employer = "DataCamp")


