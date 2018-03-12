import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight/np_height ** 2

bmi[bmi > 23]

bmi[np.logical_and(bmi > 21, bmi < 22)]
logical_or
logical_not

if bmi > 10:
    print("not so fat")
else bmi > 18 "
    print("Time to lose some weight")
else :
    print("meow meow")

sel = cars[cars['drives_right']]

