import numpy as np
np.random.seed(123)
outcomes = []
for x in range(10) :
    coint = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else :
        outcomes.append("tails")
print(outcomes)

tails = [0]
for x in ranges(10) :
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)

print(tails)

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

import matplotlib.pyplot as plt
plt.plot(random_walk)
plt.show()

