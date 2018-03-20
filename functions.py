def square(value):
    """ returns the square of a value # this is a docstring """
    new_value = value ** 2
    print(new_value)

    return new_value

num = square(4)

def raise_to_power(value1, value2)
    "" Raise value1 to the power of value2 """
    new_value = value1 ** value2
    return new_value

result = raise_to_power(2,3)
print(result) # 8

even_numbers(2,4,6) # tuple
a,b,c = even_nums

second_number = even_num[1])

def raise_both(value1, value2)
    "" Raise value1 to the power of value2 and vice versa """
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1

    new_tuple = (new_value1, new_value2)
    return new_tuple

# scopes
# global scope - defined in the main body of a script
# local scope - defined within a function - can't access outside function
# built-in scope 

# looks in local scope first, then global then built in
# can change the global scope within a function

new_val = 10
def square(value) :
    " returns the square of a number """
    global new_val
    new_value = new_val ** 2
    return new_val

square(10)
#100
new_val # 100
