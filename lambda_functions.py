# lambda functions are quick and dirty
# add parameters after keyword, colon and then function body
raise_to_power = lambda x, y; x ** y
raise_to_power(2,3) #8 

# map function take function and sequence and applies all the functions in the sequence
map(func, seq)

nums = [48, ,6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(square_all) # map object
print(list(square_all))
