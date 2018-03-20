def sqrt(x) :
    """ returns the square root of a number """
    if x < 0
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')
