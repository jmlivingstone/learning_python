error = 50.0
while error > 1 :
    error = error / 4
    print(error)


fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))

for c in "family" : 
    print(c.capitalize())

world = { "afganistan":30:55, "albania":2.77, "algergia:39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))

import numpy as np
np_height = np.array([1.73, 1.68, 1.1, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])

for val in np.nditer(meas) :
    print(val)

import pandas as pd
brics = pd.read_csv("brics.csv", index = 0
for lab, row in brics.iterrows() : 
    print(lab)
    print(row)
#    print(lab + ": " + row["capital"])
     brics.loc[lab, "name_length"] = len(row["country"])

# don't need a for loop can use apply
brics["name_length"] = brics["country"].apply(len)
