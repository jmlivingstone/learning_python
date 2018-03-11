pop = [30.55, 2.77, 39.21]
countries = ["afganistan", "albania", "algeria"]

# could use index function
ind = pop.index("albania")
countries[ind]

# but building a dictonary is better
world = {"afganistan":30.55, "albania":2.77, "algeria":39.21}

print(world["albania"])
world.keys()
# keys need to be immutable - can't be changed 

world['sealand' = 0.000027
"sealand" in world = True

del(world["sealand"])
